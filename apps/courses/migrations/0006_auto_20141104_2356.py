# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20141104_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Room Name', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(default=b'', max_length=64, verbose_name=b'Room Number', blank=True),
            preserve_default=True,
        ),
    ]
