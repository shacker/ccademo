# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20141026_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=b''),
            preserve_default=True,
        ),

        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
