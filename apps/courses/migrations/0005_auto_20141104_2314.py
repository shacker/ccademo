# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_offering_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='majors',
        ),
        migrations.RemoveField(
            model_name='program',
            name='majors',
        ),
        migrations.DeleteModel(
            name='Major',
        ),
    ]
