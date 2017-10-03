# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171002_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='label',
            field=models.CharField(choices=[('event', 'event'), ('work', 'work'), ('person', 'person'), ('organization', 'organization'), ('place', 'place'), ('page', 'page')], max_length=25),
        ),
    ]