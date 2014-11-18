# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userwidget'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccawidget',
            name='html',
            field=models.TextField(verbose_name='HTML', blank=True, null=True, help_text='Use for abitrary embeddable widgets'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ccawidget',
            name='type',
            field=models.CharField(max_length=4, default='list', choices=[('list', 'List'), ('html', 'HTML')], verbose_name='Type'),
            preserve_default=True,
        ),
    ]
