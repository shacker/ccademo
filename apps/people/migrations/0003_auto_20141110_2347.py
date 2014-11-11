# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('people', '0002_auto_20141108_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWidget',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(to='people.Profile')),
                ('widget', models.ForeignKey(to='dashboard.CCAWidget')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='dashboard_widgets',
            field=models.ManyToManyField(blank=True, null=True, help_text='This users set of Dashboard Widgets', to='dashboard.CCAWidget', through='people.UserWidget'),
            preserve_default=True,
        ),
    ]
