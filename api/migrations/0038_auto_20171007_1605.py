# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20171007_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='properties',
        ),
        migrations.RemoveField(
            model_name='recordsource',
            name='properties',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='properties',
        ),
        migrations.RemoveField(
            model_name='source',
            name='properties',
        ),
    ]
