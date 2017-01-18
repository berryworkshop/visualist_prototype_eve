# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('placefinder', '0001_initial'),
        ('timeline', '0001_initial'),
        ('catalog', '0003_auto_20170118_1228'),
        ('cms', '0003_auto_20170118_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='related_events',
            field=models.ManyToManyField(blank=True, to='timeline.Event'),
        ),
        migrations.AddField(
            model_name='venue',
            name='related_pages',
            field=models.ManyToManyField(blank=True, to='cms.Page'),
        ),
        migrations.AddField(
            model_name='venue',
            name='related_venues',
            field=models.ManyToManyField(blank=True, to='placefinder.Venue'),
        ),
        migrations.AddField(
            model_name='venue',
            name='related_works',
            field=models.ManyToManyField(blank=True, to='catalog.Work'),
        ),
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='placefinder.Address'),
        ),
    ]
