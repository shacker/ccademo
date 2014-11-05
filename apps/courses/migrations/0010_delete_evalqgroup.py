# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20141105_0710'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EvalQGroup',
        ),
    ]
