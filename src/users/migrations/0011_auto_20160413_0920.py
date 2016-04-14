# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 09:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0010_auto_20160411_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chalearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chalearn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Chalearn')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('score', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dataset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Special_Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='parent_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AlterField(
            model_name='profile_event',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AlterField(
            model_name='profile_event',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='special_issue',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='schedule_event',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='schedule_event',
            name='parent_schedule_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Schedule_Event'),
        ),
        migrations.AddField(
            model_name='publication',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Result'),
        ),
        migrations.AddField(
            model_name='partner',
            name='events',
            field=models.ManyToManyField(through='users.Challenge_Partner', to='users.Event'),
        ),
        migrations.AddField(
            model_name='new',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='data',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dataset'),
        ),
        migrations.AddField(
            model_name='challenge_partner',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='challenge_partner',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Partner'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
    ]