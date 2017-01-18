# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_work_related_contacts'),
        ('placefinder', '0001_initial'),
        ('timeline', '0001_initial'),
        ('cms', '0002_page_related_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='related_events',
            field=models.ManyToManyField(blank=True, to='timeline.Event'),
        ),
        migrations.AddField(
            model_name='work',
            name='related_pages',
            field=models.ManyToManyField(blank=True, to='cms.Page'),
        ),
        migrations.AddField(
            model_name='work',
            name='related_venues',
            field=models.ManyToManyField(blank=True, to='placefinder.Venue'),
        ),
        migrations.AddField(
            model_name='work',
            name='related_works',
            field=models.ManyToManyField(blank=True, to='catalog.Work'),
        ),
    ]
