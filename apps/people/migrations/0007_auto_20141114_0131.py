# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields
import people.models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=people.models.get_avatar_path, null=True, blank=True),
            preserve_default=True,
        ),
    ]
