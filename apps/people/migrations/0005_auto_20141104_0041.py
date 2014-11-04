# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_profile_datatel_url_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='datatel_url_field',
        ),
        migrations.AddField(
            model_name='profile',
            name='datatel_avatar_url',
            field=models.CharField(max_length=60, null=True, verbose_name=b'Datatel avatar URL', blank=True),
            preserve_default=True,
        ),
    ]
