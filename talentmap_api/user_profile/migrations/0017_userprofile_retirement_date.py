# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0016_auto_20171116_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='retirement_date',
            field=models.DateField(null=True),
        ),
    ]
