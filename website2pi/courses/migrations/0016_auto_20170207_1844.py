# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20170207_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='categor',
            new_name='category',
        ),
    ]
