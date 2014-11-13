# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_profile_dashboard_widgets'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='photos', blank=True),
            preserve_default=True,
        ),
    ]
