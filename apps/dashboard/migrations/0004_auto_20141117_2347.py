# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20141117_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccawidget',
            name='func',
            field=models.CharField(max_length=100, blank=True, null=True, verbose_name='Function to call'),
            preserve_default=True,
        ),
    ]
