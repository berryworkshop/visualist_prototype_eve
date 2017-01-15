# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 22:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('service', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('PINTEREST', 'Pinterest'), ('TUMBLR', 'Tumblr'), ('TWITTER', 'Twitter')], default='FACEBOOK', max_length=20)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Record')),
                ('synopsis', models.TextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('base.record',),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('country_code', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(999)])),
                ('area_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Contact')),
                ('name', models.CharField(max_length=100)),
                ('organization_types', models.CharField(choices=[('ARCHIVE', 'archive'), ('ASSOCIATION', 'association'), ('COMPANY', 'company'), ('ENSEMBLE', 'ensemble'), ('FOUNDATION', 'foundation'), ('GALLERY', 'gallery'), ('LIBRARY', 'library'), ('MUSEUM', 'museum'), ('SCHOOL', 'school')], default='ASSOCIATION', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('directory.contact',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='directory.Contact')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
            bases=('directory.contact',),
        ),
        migrations.AddField(
            model_name='website',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_set', to='directory.Contact'),
        ),
        migrations.AddField(
            model_name='phone',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_set', to='directory.Contact'),
        ),
        migrations.AddField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_set', to='directory.Contact'),
        ),
        migrations.AddField(
            model_name='account',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_set', to='directory.Contact'),
        ),
    ]
