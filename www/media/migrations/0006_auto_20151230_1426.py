# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20151123_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flickralbum',
            options={'ordering': ['-date_published'], 'get_latest_by': 'date_published', 'verbose_name': 'Flickr Album', 'verbose_name_plural': 'Flickr Albums'},
        ),
        migrations.AlterModelOptions(
            name='youtubevideo',
            options={'ordering': ['-date_published'], 'get_latest_by': 'date_published', 'verbose_name': 'Youtube Video', 'verbose_name_plural': 'Youtube Videos'},
        ),
    ]
