# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCAWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, default='')),
                ('mandatory', models.BooleanField(default=False, help_text='Show this widget to all users at all times.')),
                ('role_level', models.CharField(verbose_name='Role', max_length=8, default='all', choices=[('all', 'Everyone'), ('admin', 'Administrators'), ('staff', 'Staff'), ('faculty', 'Faculty'), ('student', 'Students')])),
                ('type', models.CharField(verbose_name='Type', max_length=4, default='list', choices=[('list', 'List'), ('html', 'HTML')])),
                ('linkurl', models.URLField(blank=True, help_text='Widget title links elsewhwere')),
                ('func', models.CharField(null=True, blank=True, max_length=100, verbose_name='Function to call', help_text='Use for internal data transforms to standard widget list.')),
                ('html', models.TextField(null=True, blank=True, verbose_name='HTML', help_text='Use for abitrary embeddable widgets')),
            ],
            options={
                'verbose_name_plural': 'CCA Widgets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
