# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0001_initial'),
        ('base', '0001_initial'),
        ('atlas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('length', models.DecimalField(decimal_places=3, max_digits=7)),
                ('width', models.DecimalField(decimal_places=3, max_digits=7)),
                ('height', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('dimension_unit', models.CharField(choices=[('mm', 'millimeters'), ('cm', 'centimeters'), ('m', 'meters'), ('in', 'inches'), ('ft', 'feet')], default='in', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Record')),
                ('name', models.CharField(default='Untitled', max_length=100)),
                ('synopsis', models.TextField(blank=True, max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.record',),
        ),
        migrations.CreateModel(
            name='PhysicalWork',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Work')),
                ('dimension_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.DimensionSet')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='atlas.Venue')),
            ],
            options={
                'abstract': False,
            },
            bases=('catalog.work',),
        ),
        migrations.CreateModel(
            name='TemporalWork',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Work')),
            ],
            options={
                'abstract': False,
            },
            bases=('catalog.work',),
        ),
        migrations.AddField(
            model_name='work',
            name='creators',
            field=models.ManyToManyField(blank=True, to='directory.Contact'),
        ),
    ]
