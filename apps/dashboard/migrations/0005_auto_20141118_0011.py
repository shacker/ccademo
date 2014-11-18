# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20141117_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccawidget',
            name='role_level',
            field=models.CharField(verbose_name='Type', max_length=8, default='all', choices=[('all', 'Everyone'), ('admin', 'Administrators'), ('faculty', 'Faculty'), ('students', 'Students')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ccawidget',
            name='func',
            field=models.CharField(verbose_name='Function to call', null=True, max_length=100, blank=True, help_text='Use for internal data transforms to standard widget list.'),
            preserve_default=True,
        ),
    ]
