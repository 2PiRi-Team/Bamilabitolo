# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='message',
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default='description default text'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my default location', max_length=120),
        ),
    ]