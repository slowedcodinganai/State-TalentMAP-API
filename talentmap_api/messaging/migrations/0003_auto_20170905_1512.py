# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20170830_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='read',
            new_name='is_read',
        ),
    ]
