# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0011_pressentry_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flickralbum',
            name='flickr_embed_code',
        ),
        migrations.AddField(
            model_name='flickralbum',
            name='flickr_album_url',
            field=models.CharField(default='test', help_text=b'Flickr album url', max_length=5000),
            preserve_default=False,
        ),
    ]
