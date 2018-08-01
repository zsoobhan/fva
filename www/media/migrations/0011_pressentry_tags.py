# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0010_pressentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressentry',
            name='tags',
            field=models.ManyToManyField(related_name='press_entries', to='media.Tag'),
        ),
    ]
