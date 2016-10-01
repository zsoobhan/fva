# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0008_flickralbum_flickr_embed_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickralbum',
            name='flickr_album_url',
        ),
        migrations.RemoveField(
            model_name='flickralbum',
            name='thumbnail_url',
        ),
    ]
