# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 14:34
from __future__ import unicode_literals

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chalearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('bio', models.TextField(max_length=3000)),
                ('avatar', models.ImageField(default='/static/images/default.jpg', null=True, upload_to=users.models.partner_member_avatar_path)),
                ('email', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('chalearn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Chalearn')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('file', models.FileField(null=True, upload_to=users.models.data_path)),
                ('url', models.CharField(max_length=500, null=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Data')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=users.models.workshop_gallery)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('upload_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('banner', models.ImageField(null=True, upload_to=users.models.partner_avatar_path)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('bio', models.TextField(max_length=3000)),
                ('avatar', models.ImageField(default='/static/images/default.jpg', null=True, upload_to=users.models.user_avatar_path)),
                ('affiliation', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Affiliation')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicated', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('score', models.DecimalField(decimal_places=10, max_digits=15, null=True)),
                ('dataset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Dataset')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile_Event')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Event')),
            ],
            bases=('users.event',),
        ),
        migrations.CreateModel(
            name='Special_Issue',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Event')),
            ],
            bases=('users.event',),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.Event')),
            ],
            bases=('users.event',),
        ),
        migrations.AddField(
            model_name='schedule_event',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Event'),
        ),
        migrations.AddField(
            model_name='schedule_event',
            name='parent_schedule_event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Schedule_Event'),
        ),
        migrations.AddField(
            model_name='publication',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Result'),
        ),
        migrations.AddField(
            model_name='profile_event',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_event', to='users.Event'),
        ),
        migrations.AddField(
            model_name='profile_event',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_profile', to='users.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='events',
            field=models.ManyToManyField(through='users.Profile_Event', to='users.Event'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='partner',
            name='events',
            field=models.ManyToManyField(through='users.Event_Partner', to='users.Event'),
        ),
        migrations.AddField(
            model_name='news',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Event'),
        ),
        migrations.AddField(
            model_name='event_partner',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='event_partner',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Partner'),
        ),
        migrations.AddField(
            model_name='event',
            name='chalearn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Chalearn'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Event'),
        ),
        migrations.AddField(
            model_name='data',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Dataset'),
        ),
        migrations.AddField(
            model_name='track',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Challenge'),
        ),
        migrations.AddField(
            model_name='gallery_image',
            name='workshop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Workshop'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tracks',
            field=models.ManyToManyField(through='users.Track', to='users.Challenge'),
        ),
    ]
