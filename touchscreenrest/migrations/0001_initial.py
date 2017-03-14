# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 00:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('numberOfClicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('inTopDeal', models.BooleanField(default=False)),
                ('numberOfShow', models.IntegerField(default=0)),
                ('numberOfClicks', models.IntegerField(default=0)),
                ('accomodation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementAccomodation', to='touchscreenrest.Accomodation')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('imageFile', models.ImageField(upload_to='images/')),
                ('isRestaurantLogo', models.BooleanField(default=False)),
                ('isAccomodationLogo', models.BooleanField(default=False)),
                ('accomodation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageAccomodation', to='touchscreenrest.Accomodation')),
                ('advertisement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageAdvertisement', to='touchscreenrest.Advertisement')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageDestination', to='touchscreenrest.Destination')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageEvent', to='touchscreenrest.Event')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageRestaurant', to='touchscreenrest.Accomodation')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('mapImage', models.ImageField(upload_to='maps/')),
                ('accomodation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapAccomodation', to='touchscreenrest.Event')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapEvent', to='touchscreenrest.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('numberOfClicks', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurantDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('videoFile', models.FileField(upload_to='videos/')),
                ('accomodation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoAccomodation', to='touchscreenrest.Accomodation')),
                ('advertisement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoAdvertisement', to='touchscreenrest.Advertisement')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoDestination', to='touchscreenrest.Destination')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoEvent', to='touchscreenrest.Event')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoRestaurant', to='touchscreenrest.Restaurant')),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoTour', to='touchscreenrest.Tour')),
            ],
        ),
        migrations.AddField(
            model_name='map',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapRestaurant', to='touchscreenrest.Restaurant'),
        ),
        migrations.AddField(
            model_name='image',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageTour', to='touchscreenrest.Tour'),
        ),
        migrations.AddField(
            model_name='event',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventPeriod', to='touchscreenrest.Period'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementDestination', to='touchscreenrest.Destination'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementEvent', to='touchscreenrest.Event'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementRestaurant', to='touchscreenrest.Restaurant'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementTour', to='touchscreenrest.Tour'),
        ),
        migrations.AddField(
            model_name='accomodation',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accomodationDestination', to='touchscreenrest.Destination'),
        ),
    ]
