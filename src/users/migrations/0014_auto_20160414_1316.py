# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20160414_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]