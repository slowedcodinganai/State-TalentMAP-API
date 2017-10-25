# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_location_country'),
        ('user_profile', '0013_userprofile_cdo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='primary_nationality',
            field=models.ForeignKey(help_text="The user's primary country of citizenship", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_citizens', to='organization.Country'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='secondary_nationality',
            field=models.ForeignKey(help_text="The user's secondary country of citizenship", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_citizens', to='organization.Country'),
        ),
    ]