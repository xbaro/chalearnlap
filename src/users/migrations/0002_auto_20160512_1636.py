# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]