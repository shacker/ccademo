# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userwidget'),
        ('people', '0004_auto_20141111_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dashboard_widgets',
            field=models.ManyToManyField(null=True, through='dashboard.UserWidget', help_text='This users set of Dashboard Widgets', to='dashboard.CCAWidget', blank=True),
            preserve_default=True,
        ),
    ]
