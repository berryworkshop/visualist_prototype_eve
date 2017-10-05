# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 11:54
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171003_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='value',
            field=django_date_extensions.fields.ApproximateDateField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='altitude',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='countries',
            field=models.CharField(blank=True, choices=[('CA', 'Canada'), ('FR', 'France'), ('MX', 'Mexico'), ('US', 'United States')], default='US', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, default=41.8781, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='locality',
            field=models.CharField(blank=True, default='Chicago', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, default=-87.6298, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='regions',
            field=models.CharField(blank=True, choices=[('IL', 'Illinois'), ('IN', 'Indiana'), ('MI', 'Michigan'), ('WI', 'Wisconsin')], default='IL', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='street',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='authors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='source',
            name='date',
            field=django_date_extensions.fields.ApproximateDateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='pages',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='publisher',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='recorddate',
            name='label',
            field=models.CharField(choices=[('born', 'born'), ('died', 'died'), ('started', 'started'), ('ended', 'ended'), ('lived', 'lived'), ('performed', 'performed'), ('occurred', 'occurred'), ('created', 'created')], max_length=25),
        ),
        migrations.AlterField(
            model_name='recordlocation',
            name='label',
            field=models.CharField(choices=[('born', 'born'), ('died', 'died'), ('started', 'started'), ('ended', 'ended'), ('lived', 'lived'), ('performed', 'performed'), ('occurred', 'occurred'), ('created', 'created')], max_length=25),
        ),
        migrations.AlterField(
            model_name='relation',
            name='predicate',
            field=models.CharField(choices=[('born', 'born'), ('died', 'died'), ('started', 'started'), ('ended', 'ended'), ('lived', 'lived'), ('performed', 'performed'), ('occurred', 'occurred'), ('created', 'created'), ('has_contributor', 'has contributor'), ('has_creator', 'has creator'), ('has_curator', 'has curator'), ('has_editor', 'has editor'), ('has_employee', 'has employee'), ('has_exhibitor', 'has exhibitor'), ('has_friend', 'has friend'), ('has_member', 'has member'), ('has_organizer', 'has organizer'), ('has_owner', 'has owner'), ('has_parent', 'has parent'), ('has_producer', 'has producer'), ('has_publisher', 'has publisher'), ('has_affiliation', 'has affiliation'), ('has_spouse', 'has spouse'), ('has_translator', 'has translator'), ('has_venue', 'has_venue'), ('part_of', 'part of'), ('same_as', 'same as'), ('has_record_parent', 'has record parent')], max_length=25),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('latitude', 'longitude', 'altitude')]),
        ),
    ]