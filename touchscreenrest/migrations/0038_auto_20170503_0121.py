# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0037_image_isheaderimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='courtesyOther',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Courtesy Transport Additional Info'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='parkingOther',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Secure Parking Additional Info'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='takeawayOther',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Takeaway Additional Info'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='wifiOther',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Wi-Fi Additional Info'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='courtesy',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Courtesy Transport'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='parking',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Secure Parking'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='takeaway',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='wifi',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Wi-Fi'),
        ),
    ]
