# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20160423_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='banner',
            field=models.ImageField(null=True, upload_to='partnerpics/'),
        ),
    ]
