# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0054_auto_20170614_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='numberOfShows',
            field=models.IntegerField(default=0, verbose_name='Number of shows'),
        ),
    ]