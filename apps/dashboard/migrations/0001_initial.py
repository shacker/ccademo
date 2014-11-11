# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCAWidget',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, default='')),
                ('linkurl', models.URLField(blank=True, help_text='Widget title links elsewhwere')),
                ('func', models.CharField(max_length=100, verbose_name='Function to call')),
            ],
            options={
                'verbose_name_plural': 'CCA Widgets',
            },
            bases=(models.Model,),
        ),
    ]
