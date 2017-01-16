# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_organization_members'),
        ('atlas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='occupant',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='directory.Contact'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]