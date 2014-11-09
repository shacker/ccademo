# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'notifications', '0001_initial'), (b'notifications', '0002_auto_20141108_0047'), (b'notifications', '0003_notification_level'), (b'notifications', '0004_auto_20141108_0113')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
                ('post_time', models.DateTimeField(default=datetime.datetime.now, help_text=b'Time posted on remote system', blank=True)),
                ('act_by', models.DateTimeField(help_text=b'Action due by date/time', blank=True)),
                ('resolved', models.BooleanField(default=False)),
                ('resolved_on', models.DateTimeField(help_text=b'Item marked resolved on date/time', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        migrations.AlterField(
            model_name='notification',
            name='act_by',
            field=models.DateTimeField(help_text=b'Action due by date/time', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text=b'Time posted on remote system'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='resolved_on',
            field=models.DateTimeField(help_text=b'Item marked resolved on date/time', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='level',
            field=models.CharField(default=b'info', max_length=12, choices=[(b'success', b'Success'), (b'info', b'Info'), (b'warning', b'Warning'), (b'danger', b'Danger')]),
            preserve_default=True,
        ),
    ]