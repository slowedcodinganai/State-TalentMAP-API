# Generated by Django 2.0.4 on 2018-04-18 14:36

from django.db import migrations
from talentmap_api.common.common_helpers import LANGUAGE_FORMAL_NAMES

class Migration(migrations.Migration):
    '''
    Data migration to set the formal description for any currently existing languages
    '''

    def set_formal_name(apps, schema_editor):
        Language = apps.get_model('language', 'Language')
        for lang in Language.objects.all():
            lang.formal_description = LANGUAGE_FORMAL_NAMES.get(lang.short_description, lang.short_description)
            lang.save()

    dependencies = [
        ('language', '0004_language_formal_description'),
    ]

    operations = [
        migrations.RunPython(set_formal_name),
    ]