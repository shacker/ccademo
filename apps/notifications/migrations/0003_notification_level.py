# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20141108_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='level',
            field=models.CharField(default=b'info', max_length=4, choices=[(b'sucs', b'Success'), (b'info', b'Info'), (b'warn', b'Warning'), (b'dang', b'Danger')]),
            preserve_default=True,
        ),
    ]
