# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 02:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0004_auto_20170315_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='accomodation_logos/'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementAccomodation', to='touchscreenrest.Accomodation'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementActivity', to='touchscreenrest.Activity'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementDestination', to='touchscreenrest.Destination'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementEvent', to='touchscreenrest.Event'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementPeriod', to='touchscreenrest.Period'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementRestaurant', to='touchscreenrest.Restaurant'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementTour', to='touchscreenrest.Tour'),
        ),
        migrations.AlterField(
            model_name='map',
            name='accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapAccomodation', to='touchscreenrest.Accomodation'),
        ),
        migrations.AlterField(
            model_name='map',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapEvent', to='touchscreenrest.Event'),
        ),
        migrations.AlterField(
            model_name='map',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapRestaurant', to='touchscreenrest.Restaurant'),
        ),
        migrations.AlterField(
            model_name='map',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapTour', to='touchscreenrest.Tour'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_logos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoAccomodation', to='touchscreenrest.Accomodation'),
        ),
        migrations.AlterField(
            model_name='video',
            name='advertisement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoAdvertisement', to='touchscreenrest.Advertisement'),
        ),
        migrations.AlterField(
            model_name='video',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoDestination', to='touchscreenrest.Destination'),
        ),
        migrations.AlterField(
            model_name='video',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoEvent', to='touchscreenrest.Event'),
        ),
        migrations.AlterField(
            model_name='video',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoPeriod', to='touchscreenrest.Period'),
        ),
        migrations.AlterField(
            model_name='video',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoRestaurant', to='touchscreenrest.Restaurant'),
        ),
        migrations.AlterField(
            model_name='video',
            name='tour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoTour', to='touchscreenrest.Tour'),
        ),
    ]