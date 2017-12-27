# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 18:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0021_auto_20171208_1818'),
        ('bidding', '0019_merge_20171214_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='waiver',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_waivers', to='user_profile.UserProfile'),
        )
    ]
