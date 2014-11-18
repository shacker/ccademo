# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('post_time', models.DateTimeField(default=datetime.datetime.now, help_text='Time posted on remote system')),
                ('act_by', models.DateTimeField(null=True, blank=True, help_text='Action due by date/time')),
                ('resolved', models.BooleanField(default=False)),
                ('resolved_on', models.DateTimeField(null=True, blank=True, help_text='Item marked resolved on date/time')),
                ('level', models.CharField(max_length=12, default='info', choices=[('success', 'Success'), ('info', 'Info'), ('warning', 'Warning'), ('danger', 'Danger')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='source',
            field=models.ForeignKey(to='notifications.Source'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
