# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20141103_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='person_id',
            field=models.IntegerField(help_text=b'Datatel ID', null=True, blank=True),
            preserve_default=True,
        ),
    ]
