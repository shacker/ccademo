# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20141118_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccawidget',
            name='mandatory',
            field=models.BooleanField(default=False, help_text='Show this widget to all users at all times.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ccawidget',
            name='role_level',
            field=models.CharField(verbose_name='Role', default='all', choices=[('all', 'Everyone'), ('admin', 'Administrators'), ('staff', 'Staff'), ('faculty', 'Faculty'), ('student', 'Students')], max_length=8),
            preserve_default=True,
        ),
    ]
