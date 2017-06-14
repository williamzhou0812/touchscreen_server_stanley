# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0053_advertisement_redirectto'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydestination',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
        migrations.AddField(
            model_name='essentialservice',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
        migrations.AddField(
            model_name='mining',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
        migrations.AddField(
            model_name='retail',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
        migrations.AddField(
            model_name='transportation',
            name='onlyShowSpecificAds',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Only show Specific Advertisements?'),
        ),
    ]
