# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0051_auto_20170607_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='airport',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='airport_logos/'),
        ),
    ]
