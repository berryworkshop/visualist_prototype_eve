# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0002_auto_20170115_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='HourSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='place',
            name='room',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='appointment_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='venue',
            name='hours_open',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='atlas.HourSet'),
            preserve_default=False,
        ),
    ]