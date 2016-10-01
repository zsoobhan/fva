# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_auto_20151230_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickralbum',
            name='flickr_album_id',
        ),
        migrations.AddField(
            model_name='flickralbum',
            name='flickr_album_url',
            field=models.CharField(default='XXX', help_text=b'flickr album url', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flickralbum',
            name='thumbnail_url',
            field=models.CharField(default='XXX', help_text=b'The url of the album from flickr.', max_length=32),
            preserve_default=False,
        ),
    ]
