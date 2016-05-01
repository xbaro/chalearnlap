# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 16:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160429_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=3000)),
                ('upload_date', models.DateTimeField()),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='new',
            name='event',
        ),
        migrations.DeleteModel(
            name='New',
        ),
    ]
