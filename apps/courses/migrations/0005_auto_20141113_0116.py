# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20141113_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='meeting_length',
            field=models.FloatField(blank=True, help_text='Enter as integers: For a 90 minute class enter 1.5', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
