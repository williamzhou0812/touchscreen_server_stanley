# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0060_auto_20170627_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='trivia_icons/'),
        ),
    ]
