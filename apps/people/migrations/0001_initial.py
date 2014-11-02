# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def add_groups(apps, schema_editor):
	call_command('loaddata', 'auth.group.json')


def remove_groups(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(
            add_groups,
            ),
    ]
