# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.CharField(max_length=100, db_index=True, verbose_name='URL')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('enable_comments', models.BooleanField(verbose_name='enable comments', default=False)),
                ('template_name', models.CharField(verbose_name='template name', max_length=70, blank=True, help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.")),
                ('registration_required', models.BooleanField(verbose_name='registration required', default=False, help_text='If this is checked, only logged-in users will be able to view the page.')),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ('url',),
                'verbose_name': 'flat page',
                'verbose_name_plural': 'flat pages',
            },
            bases=(models.Model,),
        ),
    ]
