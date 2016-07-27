# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20160607_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event_relation',
            old_name='event',
            new_name='event_associated',
        ),
        migrations.AddField(
            model_name='event_relation',
            name='dataset_associated',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dataset_associated', to='users.Dataset'),
        ),
    ]