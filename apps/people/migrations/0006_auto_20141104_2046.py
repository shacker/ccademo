# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20141104_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(help_text=b'A few sentences about yourself - capsule biography. No HTML allowed.', max_length=256, null=True, blank=True),
            preserve_default=True,
        )
    ]
