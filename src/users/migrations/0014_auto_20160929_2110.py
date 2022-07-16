# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-29 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20160929_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='source_code',
        ),
        migrations.AddField(
            model_name='result_user',
            name='submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Submission'),
        ),
    ]