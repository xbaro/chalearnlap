# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20160614_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='parent_event',
        ),
    ]