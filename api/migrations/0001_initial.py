# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('address_street', models.TextField()),
                ('address_locality', models.CharField(max_length=250)),
                ('address_region', models.CharField(choices=[('IL', 'Illinois'), ('IN', 'Indiana'), ('MI', 'Michigan'), ('WI', 'Wisconsin')], max_length=2)),
                ('address_postal_code', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('value', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('aspect', models.CharField(choices=[('main', 'Main'), ('recto', 'Recto'), ('verso', 'Verso'), ('detail', 'detail'), ('signature', 'signature')], default='main', max_length=25)),
                ('checksum', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('country', models.PositiveIntegerField(default=1)),
                ('area', models.PositiveIntegerField()),
                ('exchange', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
                ('extension', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('label', models.CharField(choices=[('event', 'event'), ('work', 'work'), ('person', 'person'), ('organization', 'organization'), ('page', 'page'), ('collection', 'collection')], max_length=25)),
                ('version', models.CharField(blank=True, max_length=250)),
                ('is_active', models.NullBooleanField(default=None)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_web_public', models.BooleanField(default=True)),
                ('originated_on', models.DateTimeField()),
                ('terminated_on', models.DateTimeField(blank=True)),
                ('is_group_friendly', models.NullBooleanField()),
                ('published_on', models.DateTimeField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('m', 'male'), ('f', 'female'), ('x', 'x')], max_length=1)),
                ('name_given', models.CharField(blank=True, max_length=250)),
                ('is_nonprofit', models.NullBooleanField(default=None)),
                ('is_appointment_only', models.NullBooleanField(default=None)),
                ('addresses', models.ManyToManyField(blank=True, related_name='records', to='api.Address')),
                ('emails', models.ManyToManyField(blank=True, related_name='records', to='api.Email')),
                ('images', models.ManyToManyField(blank=True, related_name='records', to='api.Image')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Image')),
                ('phones', models.ManyToManyField(blank=True, related_name='records', to='api.Phone')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicate', models.CharField(choices=[('has_category', 'has category'), ('has_contributor', 'has contributor'), ('has_creator', 'has creator'), ('has_curator', 'has curator'), ('has_employee', 'has employee'), ('has_exhibitor', 'has exhibitor'), ('has_friend', 'has friend'), ('has_member', 'has member'), ('has_organizer', 'has organizer'), ('has_owner', 'has owner'), ('has_parent', 'has parent'), ('has_place', 'has place'), ('has_producer', 'has producer'), ('has_publisher', 'has publisher')], max_length=25)),
                ('dobject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relation_direct_object', to='api.Record')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relation_subject', to='api.Record')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('service', models.CharField(choices=[('ask', 'Ask.fm'), ('facebook', 'Facebook'), ('flickr', 'Flickr'), ('foursquare', 'Foursquare'), ('github', 'GitHub'), ('googleplus', 'Google+'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('meetup', 'Meetup'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('snapchat', 'SnapChat'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('whatsapp', 'WhatsApp'), ('yelp', 'Yelp'), ('youtube', 'YouTube')], max_length=25)),
                ('value', models.CharField(max_length=250)),
                ('source', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('value', models.SlugField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=250)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Term')),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='records',
            field=models.ManyToManyField(blank=True, through='api.Relation', to='api.Record'),
        ),
        migrations.AddField(
            model_name='record',
            name='social_accounts',
            field=models.ManyToManyField(blank=True, related_name='records', to='api.SocialAccount'),
        ),
        migrations.AddField(
            model_name='record',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='records', to='api.Tag'),
        ),
        migrations.AddField(
            model_name='phone',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='image',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='email',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Term'),
        ),
        migrations.AddField(
            model_name='address',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AlterUniqueTogether(
            name='term',
            unique_together=set([('value', 'vocabulary'), ('value', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together=set([('service', 'value')]),
        ),
        migrations.AlterUniqueTogether(
            name='phone',
            unique_together=set([('area', 'exchange', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('address_street', 'address_locality', 'address_region')]),
        ),
    ]
