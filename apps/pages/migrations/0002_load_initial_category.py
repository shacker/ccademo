# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def add_category_data(apps, schema_editor):
    call_command('loaddata', 'categories.json')



class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_category_data,
            ),
    ]
