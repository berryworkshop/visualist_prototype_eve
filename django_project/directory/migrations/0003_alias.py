# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_organization_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.Contact')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]