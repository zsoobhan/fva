# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0012_auto_20181228_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='flickralbum',
            name='flickr_thumbnail_url',
            field=models.CharField(default='xxx', help_text=b'looks like https://farm2.staticflickr.com/1907/43656216960_4a56163a49_m.jpg', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flickralbum',
            name='flickr_album_url',
            field=models.CharField(help_text=b'Flickr album url', max_length=1024),
        ),
    ]
