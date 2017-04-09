# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0019_auto_20170407_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isDisplayVideo',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Is display Video?'),
        ),
    ]