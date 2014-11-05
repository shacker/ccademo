# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20141105_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering',
            name='eval_group',
        ),
        migrations.RemoveField(
            model_name='offering',
            name='instr_eval_group',
        ),
    ]
