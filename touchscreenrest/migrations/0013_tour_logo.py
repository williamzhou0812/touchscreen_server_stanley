# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0012_auto_20170326_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='tour_logos/'),
        ),
    ]
