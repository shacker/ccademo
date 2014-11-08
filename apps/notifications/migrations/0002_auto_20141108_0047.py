# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='act_by',
            field=models.DateTimeField(help_text=b'Action due by date/time', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text=b'Time posted on remote system'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='resolved_on',
            field=models.DateTimeField(help_text=b'Item marked resolved on date/time', null=True, blank=True),
            preserve_default=True,
        ),
    ]
