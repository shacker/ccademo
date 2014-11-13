# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20141113_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.CharField(max_length=12),
            preserve_default=True,
        ),
    ]
