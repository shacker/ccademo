# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwidget',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userwidget',
            name='widget',
            field=models.ForeignKey(to='dashboard.CCAWidget'),
            preserve_default=True,
        ),
    ]
