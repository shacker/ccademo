# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.utils import timezone



class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20141026_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=b'slug'),
            preserve_default=True,
        )
    ]
