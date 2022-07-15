# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-21 16:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_main_org'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chalearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_text', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CIMLBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('content', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
