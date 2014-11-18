# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='instructors',
            field=models.ManyToManyField(to='people.Instructor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='course',
            field=models.ForeignKey(to='courses.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='days_of_week',
            field=models.ManyToManyField(null=True, blank=True, to='courses.Days'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='instructors',
            field=models.ManyToManyField(blank=True, to='people.Instructor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='location',
            field=models.ForeignKey(to='courses.Room', help_text='If location is mixed, such as &quot;Monday in the Mission, Thursday RM 104&quot; then select Other as location and fill in Other Location field.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='sec_term',
            field=models.ForeignKey(to='courses.Semester'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offering',
            name='students',
            field=models.ManyToManyField(blank=True, to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material',
            name='offering',
            field=models.ForeignKey(to='courses.Offering'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='programs',
            field=models.ManyToManyField(null=True, blank=True, to='courses.Program'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='builder',
            name='offering',
            field=models.ForeignKey(to='courses.Offering'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='builder',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='offering',
            field=models.ForeignKey(to='courses.Offering'),
            preserve_default=True,
        ),
    ]
