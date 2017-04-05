# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 01:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0013_tour_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('numberOfClicks', models.IntegerField(default=0, verbose_name='Number of clicks')),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activityDestinationActivity', to='touchscreenrest.Activity')),
            ],
            options={
                'verbose_name': 'Destination for Activity',
            },
        ),
        migrations.DeleteModel(
            name='Deal',
        ),
        migrations.AddField(
            model_name='tour',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tourDestination', to='touchscreenrest.Destination'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='activityDestination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementActivityDestination', to='touchscreenrest.ActivityDestination'),
        ),
        migrations.AddField(
            model_name='image',
            name='activityDestination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageActivityDestination', to='touchscreenrest.ActivityDestination'),
        ),
        migrations.AddField(
            model_name='tour',
            name='activityDestination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tourActivityDestination', to='touchscreenrest.ActivityDestination'),
        ),
        migrations.AddField(
            model_name='video',
            name='activityDestination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoActivityDestination', to='touchscreenrest.ActivityDestination'),
        ),
    ]