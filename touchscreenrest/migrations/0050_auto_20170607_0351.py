# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0049_advertisement_firstlevelad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['order', 'pk']},
        ),
        migrations.AddField(
            model_name='advertisement',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Advertisement order display'),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Accommodation order display'),
        ),
    ]