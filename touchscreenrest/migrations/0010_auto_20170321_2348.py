# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0009_auto_20170321_2225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='essentialservice',
            options={'verbose_name': 'Essential Service'},
        ),
        migrations.AlterModelOptions(
            name='mining',
            options={'verbose_name': 'Mining & Resource'},
        ),
        migrations.AlterModelOptions(
            name='transportation',
            options={'verbose_name': 'Car Hire & Transport'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementEssentialService', to='touchscreenrest.EssentialService', verbose_name='Essential Services'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementMining', to='touchscreenrest.Mining', verbose_name='Mining & Resources'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementTransportation', to='touchscreenrest.Transportation', verbose_name='Car Hire & Transportation'),
        ),
        migrations.AlterField(
            model_name='image',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageEssentialService', to='touchscreenrest.EssentialService', verbose_name='Essential Services'),
        ),
        migrations.AlterField(
            model_name='image',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageMining', to='touchscreenrest.Mining', verbose_name='Mining & Resources'),
        ),
        migrations.AlterField(
            model_name='image',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageTransportation', to='touchscreenrest.Transportation', verbose_name='Car Hire & Transportation'),
        ),
        migrations.AlterField(
            model_name='map',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapEssentialService', to='touchscreenrest.EssentialService', verbose_name='Essential Services'),
        ),
        migrations.AlterField(
            model_name='map',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapMining', to='touchscreenrest.Mining', verbose_name='Mining & Resources'),
        ),
        migrations.AlterField(
            model_name='map',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapTransportation', to='touchscreenrest.Transportation', verbose_name='Car Hire & Transportation'),
        ),
        migrations.AlterField(
            model_name='video',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoEssentialService', to='touchscreenrest.EssentialService', verbose_name='Essential Services'),
        ),
        migrations.AlterField(
            model_name='video',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoMining', to='touchscreenrest.Mining', verbose_name='Mining & Resources'),
        ),
        migrations.AlterField(
            model_name='video',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoTransportation', to='touchscreenrest.Transportation', verbose_name='Car Hire & Transportation'),
        ),
    ]