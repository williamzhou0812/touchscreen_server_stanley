# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0036_auto_20170501_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='isHeaderImage',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Is Header Image?'),
        ),
    ]