# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20171002_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecordDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(choices=[('is_born', 'is born'), ('dies', 'dies'), ('starts', 'starts'), ('ends', 'ends'), ('lives', 'lives'), ('performs', 'performs'), ('occurs', 'occurs'), ('is', 'is'), ('is_created', 'is created')], max_length=25)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecordLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(choices=[('is_born', 'is born'), ('dies', 'dies'), ('starts', 'starts'), ('ends', 'ends'), ('lives', 'lives'), ('performs', 'performs'), ('occurs', 'occurs'), ('is', 'is'), ('is_created', 'is created')], max_length=25)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecordSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('accessed', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='relation',
            name='properties',
        ),
        migrations.AddField(
            model_name='relation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relation',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='label',
            field=models.CharField(choices=[('event', 'event'), ('work', 'work'), ('person', 'person'), ('organization', 'organization')], max_length=25),
        ),
        migrations.AlterField(
            model_name='relation',
            name='predicate',
            field=models.CharField(choices=[('is_born', 'is born'), ('dies', 'dies'), ('starts', 'starts'), ('ends', 'ends'), ('lives', 'lives'), ('performs', 'performs'), ('occurs', 'occurs'), ('is', 'is'), ('is_created', 'is created'), ('has_contributor', 'has contributor'), ('has_creator', 'has creator'), ('has_curator', 'has curator'), ('has_editor', 'has editor'), ('has_employee', 'has employee'), ('has_exhibitor', 'has exhibitor'), ('has_friend', 'has friend'), ('has_member', 'has member'), ('has_organizer', 'has organizer'), ('has_owner', 'has owner'), ('has_parent', 'has parent'), ('has_producer', 'has producer'), ('has_publisher', 'has publisher'), ('has_affiliation', 'has affiliation'), ('has_spouse', 'has spouse'), ('has_translator', 'has translator'), ('has_venue', 'has_venue'), ('part_of', 'part of'), ('same_as', 'same as'), ('has_record_parent', 'has record parent')], max_length=25),
        ),
        migrations.AddField(
            model_name='recordsource',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='recordsource',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Source'),
        ),
        migrations.AddField(
            model_name='recordlocation',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='recorddate',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Record'),
        ),
        migrations.AddField(
            model_name='record',
            name='dates',
            field=models.ManyToManyField(through='api.RecordDate', to='api.Date'),
        ),
        migrations.AddField(
            model_name='record',
            name='locations',
            field=models.ManyToManyField(through='api.RecordLocation', to='api.Location'),
        ),
        migrations.AddField(
            model_name='record',
            name='sources',
            field=models.ManyToManyField(through='api.RecordSource', to='api.Source'),
        ),
        migrations.AddField(
            model_name='relation',
            name='dates',
            field=models.ManyToManyField(to='api.Date'),
        ),
        migrations.AddField(
            model_name='relation',
            name='locations',
            field=models.ManyToManyField(to='api.Location'),
        ),
        migrations.AddField(
            model_name='relation',
            name='sources',
            field=models.ManyToManyField(to='api.Source'),
        ),
    ]