# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20141111_2018'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWidget',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(to='people.Profile')),
                ('widget', models.ForeignKey(to='dashboard.CCAWidget')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
