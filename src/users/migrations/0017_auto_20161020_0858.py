# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-20 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20161005_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='sub_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='submission',
            name='rank',
            field=models.IntegerField(null=True),
        ),
    ]
