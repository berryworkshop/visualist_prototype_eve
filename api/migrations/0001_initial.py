# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 02:44
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
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address_street', models.TextField()),
                ('address_locality', models.TextField()),
                ('address_region', models.TextField(choices=[('IL', 'Illinois'), ('IN', 'Indiana'), ('MI', 'Michigan'), ('WI', 'Wisconsin')])),
                ('address_postal_code', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.TextField()),
                ('aspect', models.TextField(choices=[('main', 'Main'), ('recto', 'Recto'), ('verso', 'Verso'), ('detail', 'detail'), ('signature', 'signature')], default='main')),
                ('checksum', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.TextField(choices=[('US', 'United States of America'), ('CA', 'Canada'), ('MX', 'Mexico')])),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('country', models.PositiveIntegerField()),
                ('area', models.PositiveIntegerField()),
                ('exchange', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
                ('extension', models.PositiveIntegerField()),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('featured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('web_public', models.BooleanField(default=True)),
                ('same_as', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.TextField()),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('service', models.TextField(choices=[('ask', 'Ask.fm'), ('facebook', 'Facebook'), ('flickr', 'Flickr'), ('foursquare', 'Foursquare'), ('github', 'GitHub'), ('googleplus', 'Google+'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('meetup', 'Meetup'), ('pinterest', 'Pinterest'), ('reddit', 'Reddit'), ('snapchat', 'SnapChat'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('whatsapp', 'WhatsApp'), ('yelp', 'Yelp'), ('youtube', 'YouTube')])),
                ('value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.SlugField()),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Record')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.record',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Record')),
                ('name', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('status', models.TextField(choices=[('active', 'active'), ('cancelled', 'cancelled')], default='active')),
                ('group_friendly', models.NullBooleanField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.record',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Record')),
                ('name', models.TextField()),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Snippet')),
                ('events', models.ManyToManyField(related_name='has_venue', to='api.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.record',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Record')),
                ('name', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.record',),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Record')),
                ('name', models.TextField()),
                ('completed', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('version', models.TextField()),
                ('url', models.URLField()),
                ('created_at', models.ManyToManyField(related_name='works_created_here', to='api.Place')),
                ('location', models.ManyToManyField(related_name='works_here', to='api.Place')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.record',),
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='account_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='api.Record'),
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='record',
            name='categories',
            field=models.ManyToManyField(to='api.Category'),
        ),
        migrations.AddField(
            model_name='record',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Snippet'),
        ),
        migrations.AddField(
            model_name='record',
            name='identifiers',
            field=models.ManyToManyField(to='api.Identifier'),
        ),
        migrations.AddField(
            model_name='record',
            name='images',
            field=models.ManyToManyField(to='api.Image'),
        ),
        migrations.AddField(
            model_name='record',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='record',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='record',
            name='tags',
            field=models.ManyToManyField(to='api.Tag'),
        ),
        migrations.AddField(
            model_name='phone',
            name='phone_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='phone',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='nationality',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='image',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='image',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='identifier',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='email',
            name='email_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='email',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='email',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='category',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Category'),
        ),
        migrations.AddField(
            model_name='category',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Nationality'),
        ),
        migrations.AddField(
            model_name='address',
            name='address_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='api.Record'),
        ),
        migrations.AddField(
            model_name='address',
            name='license',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.License'),
        ),
        migrations.AddField(
            model_name='address',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Resource'),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Post')),
                ('records', models.ManyToManyField(to='api.Record')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.post',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Entity')),
                ('name', models.TextField()),
                ('founded', models.DateTimeField()),
                ('dissolved', models.DateTimeField()),
                ('nonprofit', models.NullBooleanField()),
                ('appointment_only', models.BooleanField(default=False)),
                ('hours', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.entity',),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Post')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Snippet')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.post',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Entity')),
                ('name_first', models.TextField()),
                ('name_last', models.TextField()),
                ('born', models.DateTimeField()),
                ('died', models.DateTimeField()),
                ('gender', models.TextField(blank=True, choices=[('m', 'male'), ('f', 'female'), ('x', 'x')])),
                ('born_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birthplace_of', to='api.Place')),
                ('died_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deathplace_of', to='api.Place')),
                ('friends', models.ManyToManyField(related_name='_person_friends_+', to='api.Person')),
                ('nationalities', models.ManyToManyField(to='api.Nationality')),
                ('parents', models.ManyToManyField(related_name='_person_parents_+', to='api.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=('api.entity',),
        ),
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Post'),
        ),
        migrations.AddField(
            model_name='event',
            name='contributors',
            field=models.ManyToManyField(related_name='contributor_to', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='curators',
            field=models.ManyToManyField(related_name='curator_of', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='exhibitors',
            field=models.ManyToManyField(related_name='exhibitor_at', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizers',
            field=models.ManyToManyField(related_name='organizer_of', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='producers',
            field=models.ManyToManyField(related_name='producer_of', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='entity',
            name='works',
            field=models.ManyToManyField(related_name='creator', to='api.Work'),
        ),
        migrations.AddField(
            model_name='organization',
            name='artists',
            field=models.ManyToManyField(related_name='represented_by', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='organization',
            name='employees',
            field=models.ManyToManyField(related_name='employed_by', to='api.Person'),
        ),
        migrations.AddField(
            model_name='organization',
            name='founded_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place'),
        ),
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Image'),
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='member_of', to='api.Entity'),
        ),
        migrations.AddField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Organization'),
        ),
    ]