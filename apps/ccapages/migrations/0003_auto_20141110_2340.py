# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapages', '0002_auto_20141110_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
            preserve_default=True,
        ),
    ]
