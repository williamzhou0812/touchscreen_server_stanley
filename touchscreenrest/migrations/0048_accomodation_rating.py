# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0047_auto_20170601_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]