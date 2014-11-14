# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_builder'),
        ('people', '0007_auto_20141114_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='planned_classes',
            field=models.ManyToManyField(to='courses.Builder', related_name='planned_classes', null=True, help_text='Classes this user intends to take', blank=True),
            preserve_default=True,
        ),
    ]
