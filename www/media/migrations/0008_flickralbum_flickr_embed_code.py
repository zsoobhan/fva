# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0007_auto_20161001_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='flickralbum',
            name='flickr_embed_code',
            field=models.CharField(default='yyy', help_text=b'Flickr embed code', max_length=1024),
            preserve_default=False,
        ),
    ]
