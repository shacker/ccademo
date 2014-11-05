# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20141104_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering',
            name='instructors',
            field=models.ManyToManyField(to='people.Instructor', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='students',
            field=models.ManyToManyField(to='people.Profile', null=True, blank=True),
            preserve_default=True,
        ),
    ]
