# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0011_auto_20170322_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tourActivity', to='touchscreenrest.Activity'),
        ),
    ]
