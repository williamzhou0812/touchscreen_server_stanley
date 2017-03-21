# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 22:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('touchscreenrest', '0008_auto_20170320_0212'),
    ]

    operations = [
        migrations.CreateModel(
            name='EssentialService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='retail_logos/')),
                ('numberOfClicks', models.IntegerField(default=0, verbose_name='Number of clicks')),
                ('order', models.IntegerField(default=0, verbose_name='Essential Service order display')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='essentialServiceDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Mining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='mining_logos/')),
                ('numberOfClicks', models.IntegerField(default=0, verbose_name='Number of clicks')),
                ('order', models.IntegerField(default=0, verbose_name='Mining order display')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miningDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Retail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='retail_logos/')),
                ('numberOfClicks', models.IntegerField(default=0, verbose_name='Number of clicks')),
                ('order', models.IntegerField(default=0, verbose_name='Retail order display')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='transportation_logos/')),
                ('numberOfClicks', models.IntegerField(default=0, verbose_name='Number of clicks')),
                ('order', models.IntegerField(default=0, verbose_name='Transportation order display')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportationDestination', to='touchscreenrest.Destination')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementEssentialService', to='touchscreenrest.EssentialService'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementMining', to='touchscreenrest.Mining'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementRetail', to='touchscreenrest.Retail'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisementTransportation', to='touchscreenrest.Transportation'),
        ),
        migrations.AddField(
            model_name='image',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageEssentialService', to='touchscreenrest.EssentialService'),
        ),
        migrations.AddField(
            model_name='image',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageMining', to='touchscreenrest.Mining'),
        ),
        migrations.AddField(
            model_name='image',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageRetail', to='touchscreenrest.Retail'),
        ),
        migrations.AddField(
            model_name='image',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageTransportation', to='touchscreenrest.Transportation'),
        ),
        migrations.AddField(
            model_name='map',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapEssentialService', to='touchscreenrest.EssentialService'),
        ),
        migrations.AddField(
            model_name='map',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapMining', to='touchscreenrest.Mining'),
        ),
        migrations.AddField(
            model_name='map',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapRetail', to='touchscreenrest.Retail'),
        ),
        migrations.AddField(
            model_name='map',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mapTransportation', to='touchscreenrest.Transportation'),
        ),
        migrations.AddField(
            model_name='video',
            name='essentialservice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoEssentialService', to='touchscreenrest.EssentialService'),
        ),
        migrations.AddField(
            model_name='video',
            name='mining',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoMining', to='touchscreenrest.Mining'),
        ),
        migrations.AddField(
            model_name='video',
            name='retail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoRetail', to='touchscreenrest.Retail'),
        ),
        migrations.AddField(
            model_name='video',
            name='transportation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videoTransportation', to='touchscreenrest.Transportation'),
        ),
    ]