# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20141026_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
