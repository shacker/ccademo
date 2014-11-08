# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'news', '0001_initial'), (b'news', '0002_auto_20141026_0044'), (b'news', '0003_auto_20141026_0052'), (b'news', '0004_auto_20141026_0707'), (b'news', '0005_auto_20141026_0717')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('title', models.CharField(default=b'Unknown Title', max_length=100)),
                ('body', models.TextField(help_text=b'Story text')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 8, 1, 53, 5, 163513), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
