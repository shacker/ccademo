# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_squashed_0005_auto_20141026_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(help_text='Story text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
