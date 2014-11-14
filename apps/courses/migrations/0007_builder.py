# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20141114_0131'),
        ('courses', '0006_auto_20141113_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('offering', models.ForeignKey(to='courses.Offering')),
                ('profile', models.ForeignKey(to='people.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
