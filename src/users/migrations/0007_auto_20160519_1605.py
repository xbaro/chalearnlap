# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160519_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/static/images/default.jpg', null=True, upload_to=users.models.user_avatar_path),
        ),
    ]