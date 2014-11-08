# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_squashed_0004_auto_20141108_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='act_by',
            field=models.DateTimeField(null=True, help_text='Action due by date/time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(default='info', choices=[('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')], max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Time posted on remote system'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='resolved_on',
            field=models.DateTimeField(null=True, help_text='Item marked resolved on date/time', blank=True),
            preserve_default=True,
        ),
    ]
