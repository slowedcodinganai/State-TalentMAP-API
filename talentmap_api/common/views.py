from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist

from talentmap_api.position.models import Position


class ShareView(APIView):
    '''
    Shares a TalentMAP element

    Post method accepts an object with at minimum the following parameters:
    * type - the type of object to be shared (position)
    * mode - the mode of sharing (internal, email)
    * id - the id of the object to be shared
    * email - the email to send the share to, if mode is email
    * user - the user id to share the item with, if mode is internal
    '''

    AVAILABLE_MODES = ["email", "internal"]
    AVAILABLE_TYPES = {
        "position": Position
    }

    def post(self, request, format=None):
        valid, error = self.validate(request)

        if valid:
            response = None
            if request.data.get("mode") == "email":
                response = self.email_share(request.data.get("email"), request.data.get("type"), request.data.get("id"))
            elif request.data.get("mode") == "internal":
                response = self.internal_share(request.data.get("user"), request.data.get("type"), request.data.get("id"))
            return response
        else:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)

    def validate(self, request):
        '''
        Validates that the request is a properly formatted share request, returning (True, None) in that case.
        If the request fails validation, it will return (False, String) where the second item of the tuple is
        a string explanation of the validation error.
        '''
        if "mode" not in request.data:
            return (False, "POSTs to this endpoint require the mode parameter")
        elif request.data.get("mode") not in self.AVAILABLE_MODES:
            return (False, f"Mode must be one of the following: {','.join(self.AVAILABLE_MODES)}")

        if "type" not in request.data:
            return (False, "POSTs to this endpoint require the type parameter")
        elif request.data.get("type") not in self.AVAILABLE_TYPES.keys():
            return (False, f"Type must be one of the following: {','.join(self.AVAILABLE_TYPES.keys())}")

        if "id" not in request.data:
            return (False, "id of sharable object must be specified")

        # E-mail specific validations
        if request.data.get("mode") == "email":
            if "email" not in request.data:
                return (False, "E-mail shares require an 'email' parameter to be specified")

        # Internal specific validations
        if request.data.get("mode") == "internal":
            if "user" not in request.data:
                return (False, "Internal shares require a 'user' parameter to be specified")

        return (True, None)

    def email_share(self, email, type, id):
        # Get our e-mail formatter
        formatter = self.get_email_formatter(type)
        instance = None

        # Attempt to get the object instance we want to share
        try:
            instance = self.AVAILABLE_TYPES[type].objects.get(id=id)
        except ObjectDoesNotExist:
            # If it doesn't exist, respond with a 404
            return Response({"message": f"Object with id {id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Create our e-mail body
        email_body = {
            "to": email,
            "subject": f"[TalentMAP] Shared {type}",
            "body": formatter(instance)
        }

        # TODO: Implement actual e-mail sending here when avaiable e-mail servers are clarified

        # Return a 202 ACCEPTED with a copy of the email body
        return Response({"email": email_body}, status=status.HTTP_202_ACCEPTED)

    def internal_share(self, user, type, id):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def get_email_formatter(self, type):
        formatter = None
        if type == "position":
            def formatter(instance):
                return f"This position has been shared with you via TalentMAP\n\n" \
                       f"\tPosition Number: {instance.position_number}\n\tPosition Title: {instance.title}\n" \
                       f"\tPost: {instance.post}"
        return formatter
