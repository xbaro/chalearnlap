# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 19:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160407_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile_event',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='users.Event'),
        ),
        migrations.AlterField(
            model_name='profile_event',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.Profile'),
        ),
    ]
