# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20141113_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering',
            name='meeting_length',
        ),
        migrations.AddField(
            model_name='offering',
            name='duration',
            field=models.FloatField(help_text='Class meeting length. Enter as integers: For a 90 minute class enter 1.5', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='start_time',
            field=models.TimeField(help_text='Use military time, e.g. 08:30:00 for 8:30 am', blank=True, null=True),
            preserve_default=True,
        ),
    ]
