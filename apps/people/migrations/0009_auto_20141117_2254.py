# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_profile_planned_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, help_text='Your Facebook username', null=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, help_text='Your twitter username', null=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumni',
            name='first_job',
            field=models.CharField(blank=True, verbose_name='First job out of CCA', null=True, max_length=384),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumni',
            name='pub_display',
            field=models.BooleanField(verbose_name='Display Option', default=True, help_text='If unchecked, record will be hidden even from other CCA alumni, faculty, students and staff.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumni',
            name='suggestions',
            field=models.TextField(blank=True, help_text="Do you have suggestions for us about what you'd like to get out of the CCA Alumni Organization? If so, please write us a note and we'll try to incorporate your idea.", null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='allow_contact',
            field=models.BooleanField(default=True, help_text='Allow the public to contact you through the CCA Intranet.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='salutation',
            field=models.IntegerField(blank=True, help_text='e.g. Mrs., Ms., Mr.', null=True, max_length=2, choices=[(1, 'Mr.'), (2, 'Mrs.'), (3, 'Ms.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='suffix',
            field=models.IntegerField(blank=True, help_text='e.g. Dr., Phd.', null=True, max_length=2, choices=[(1, 'Ph.D'), (2, 'MD')]),
            preserve_default=True,
        ),
    ]
