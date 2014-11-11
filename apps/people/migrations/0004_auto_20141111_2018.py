# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20141110_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwidget',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='userwidget',
            name='widget',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dashboard_widgets',
        ),
        migrations.DeleteModel(
            name='UserWidget',
        ),
    ]
