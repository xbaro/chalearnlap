# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_schedule_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_event',
            name='parent_schedule_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Schedule_Event'),
        ),
    ]
