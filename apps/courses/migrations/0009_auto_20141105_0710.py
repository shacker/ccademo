# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20141105_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evallog',
            name='offering',
        ),
        migrations.RemoveField(
            model_name='evallog',
            name='q_group',
        ),
        migrations.RemoveField(
            model_name='evallog',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='evallog',
            name='user',
        ),
        migrations.DeleteModel(
            name='EvalLog',
        ),
        migrations.RemoveField(
            model_name='evalquestion',
            name='q_group',
        ),
        migrations.RemoveField(
            model_name='evalquestion',
            name='semester_added',
        ),
        migrations.RemoveField(
            model_name='evalresponse',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='evalresponse',
            name='offering',
        ),
        migrations.RemoveField(
            model_name='evalresponse',
            name='q_group',
        ),
        migrations.RemoveField(
            model_name='evalresponse',
            name='question',
        ),
        migrations.DeleteModel(
            name='EvalQuestion',
        ),
        migrations.RemoveField(
            model_name='evalresponse',
            name='semester',
        ),
        migrations.DeleteModel(
            name='EvalResponse',
        ),
    ]
