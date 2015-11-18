# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(help_text=b'Your message goes here.', max_length=4096)),
                ('name', models.CharField(help_text=b'Your name goes here.', max_length=64)),
                ('phone_number', models.CharField(help_text=b'Your phone number goes here.', max_length=16, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('upload_file', s3direct.fields.S3DirectField()),
            ],
        ),
    ]
