# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 01:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0022_auto_20170407_0059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accomodation',
            options={'verbose_name': 'Accommodation', 'verbose_name_plural': 'Accommodation'},
        ),
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'Activity', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='transportation',
            options={'verbose_name': 'Car Hire & Transport', 'verbose_name_plural': 'Car Hire & Transport'},
        ),
    ]
