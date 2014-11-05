# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0007_auto_20141104_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('long_title', models.CharField(max_length=100)),
                ('internal_title', models.CharField(max_length=16)),
                ('short_title_formatted', models.CharField(max_length=64)),
                ('section', models.IntegerField(verbose_name=b'Section', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23'), (24, b'24'), (25, b'25'), (26, b'26'), (27, b'27'), (28, b'28'), (29, b'29'), (30, b'30'), (31, b'31'), (32, b'32'), (33, b'33'), (34, b'34'), (35, b'35'), (36, b'36'), (37, b'37'), (38, b'38'), (39, b'39'), (40, b'40'), (41, b'41'), (42, b'42'), (43, b'43'), (44, b'44'), (45, b'45'), (46, b'46'), (47, b'47'), (48, b'48'), (49, b'49'), (50, b'50'), (51, b'51'), (52, b'52'), (53, b'53'), (54, b'54'), (55, b'55'), (56, b'56'), (57, b'57'), (58, b'58'), (59, b'59'), (60, b'60'), (61, b'61'), (62, b'62'), (63, b'63'), (64, b'64'), (65, b'65'), (66, b'66'), (67, b'67'), (68, b'68'), (69, b'69'), (70, b'70'), (71, b'71'), (72, b'72'), (73, b'73'), (74, b'74'), (75, b'75'), (76, b'76'), (77, b'77'), (78, b'78'), (79, b'79'), (80, b'80'), (81, b'81'), (82, b'82'), (83, b'83'), (84, b'84'), (85, b'85'), (86, b'86'), (87, b'87'), (88, b'88'), (89, b'89'), (90, b'90'), (91, b'91'), (92, b'92'), (93, b'93'), (94, b'94'), (95, b'95'), (96, b'96'), (97, b'97'), (98, b'98'), (99, b'99'), (100, b'100')])),
                ('units', models.IntegerField(choices=[(1, b'1'), (15, b'1.5'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (99, b'var')])),
                ('course_type', models.IntegerField(choices=[(1, b'Non-Graduate / General Courses'), (2, b'Required Courses'), (3, b'Background Courses'), (4, b'Advanced Reporting Courses'), (5, b'Skills Courses'), (6, b'Recommended Outside Classes')])),
                ('description', models.TextField()),
                ('restrictions', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvalLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Evaluation Log Entry',
                'verbose_name_plural': 'Evaluation Logs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvalQGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q_group_type', models.IntegerField(verbose_name=b'Question set type', choices=[(0, b'Course'), (1, b'Instructor'), (2, b'Other')])),
                ('q_group_title', models.CharField(max_length=765)),
                ('page_header', models.TextField()),
                ('active', models.BooleanField(default=1, verbose_name=b'Active')),
            ],
            options={
                'verbose_name': 'Evaluation Question Set',
                'verbose_name_plural': 'Evaluation Question Sets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvalQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(choices=[(0, b'Text'), (1, b'Rating')])),
                ('order', models.IntegerField(help_text=b'If blank, position of this question in eval cannot be guaranteed.', null=True, blank=True)),
                ('mothball', models.BooleanField(default=False, help_text=b'Rather than delete old questions, mothball them instead. That will prevent them from appearing on new evaluations, but wont mess with stats in old reports.')),
                ('text', models.TextField()),
                ('q_group', models.ForeignKey(verbose_name=b'In question group', to='courses.EvalQGroup')),
            ],
            options={
                'verbose_name': 'Evaluation Question',
                'verbose_name_plural': 'Evaluation Questions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EvalResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.IntegerField()),
                ('text_response', models.TextField(null=True, blank=True)),
                ('numeric_response', models.IntegerField(null=True, blank=True)),
                ('instructor', models.ForeignKey(blank=True, to='people.Instructor', null=True)),
            ],
            options={
                'verbose_name': 'Evaluation Response',
                'verbose_name_plural': 'Evaluation Responses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('obtain_at', models.CharField(max_length=100, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('cost', models.DecimalField(null=True, verbose_name=b'Approximate Cost', max_digits=8, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_sec_id', models.IntegerField(unique=True, verbose_name=b'Section ID (from datatel)')),
                ('title', models.CharField(help_text=b'If present, overrides same field in Course model.', max_length=384, null=True, blank=True)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('location_other', models.CharField(max_length=100, blank=True)),
                ('grading', models.TextField(null=True, blank=True)),
                ('policies', models.TextField(null=True, blank=True)),
                ('fee', models.BooleanField(default=False, help_text=b'Fee required to take this course?')),
                ('enroll_lim', models.IntegerField(blank=True, help_text=b'Enrollment limit for this course (select nothing if there isn&apos;t one.)', null=True, verbose_name=b'Enrollment limit', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23'), (24, b'24'), (25, b'25'), (26, b'26'), (27, b'27'), (28, b'28'), (29, b'29'), (30, b'30'), (31, b'31'), (32, b'32'), (33, b'33'), (34, b'34'), (35, b'35'), (36, b'36'), (37, b'37'), (38, b'38'), (39, b'39'), (40, b'40'), (41, b'41'), (42, b'42'), (43, b'43'), (44, b'44'), (45, b'45'), (46, b'46'), (47, b'47'), (48, b'48'), (49, b'49'), (50, b'50'), (51, b'51'), (52, b'52'), (53, b'53'), (54, b'54'), (55, b'55'), (56, b'56'), (57, b'57'), (58, b'58'), (59, b'59'), (60, b'60'), (61, b'61'), (62, b'62'), (63, b'63'), (64, b'64'), (65, b'65'), (66, b'66'), (67, b'67'), (68, b'68'), (69, b'69'), (70, b'70'), (71, b'71'), (72, b'72'), (73, b'73'), (74, b'74'), (75, b'75'), (76, b'76'), (77, b'77'), (78, b'78'), (79, b'79'), (80, b'80'), (81, b'81'), (82, b'82'), (83, b'83'), (84, b'84'), (85, b'85'), (86, b'86'), (87, b'87'), (88, b'88'), (89, b'89'), (90, b'90'), (91, b'91'), (92, b'92'), (93, b'93'), (94, b'94'), (95, b'95'), (96, b'96'), (97, b'97'), (98, b'98'), (99, b'99'), (100, b'100')])),
                ('description_override', models.TextField(help_text=b'If present, overrides same field in Course model.', null=True, blank=True)),
                ('restrictions_override', models.TextField(help_text=b'If present, overrides same field in Course model.', null=True, blank=True)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('eval_group', models.ForeignKey(related_name='course_eval_group', blank=True, to='courses.EvalQGroup', help_text=b'Which COURSE evaluations question set should this course be evaluated with at the end of the semester?', null=True, verbose_name=b'Course evaluation question set')),
                ('instr_eval_group', models.ForeignKey(related_name='instr_eval_group', default=2, to='courses.EvalQGroup', blank=True, help_text=b'Which INSTRUCTOR evaluations question set should this course be evaluated with at the end of the semester?', null=True, verbose_name=b'Instructor evaluation question set')),
                ('instructors', models.ManyToManyField(to='people.Instructor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('instructors', models.ManyToManyField(to='people.Instructor')),
                ('majors', models.ManyToManyField(to='courses.Major', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=64, verbose_name=b'Room Number', blank=True)),
                ('has_screen', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=96)),
                ('current', models.NullBooleanField(help_text=b'Select &quot;Yes&quot; for the current semester, &quot;Unknown&quot; for all others. Ignore the &quot;No&quot; option. Only one semester may be marked current at a time.', unique=True)),
                ('ord_by', models.IntegerField(null=True, blank=True)),
                ('live', models.BooleanField(default=False, help_text=b'When checked, this semester&apos;s schedule will appear on the public site.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='offering',
            name='location',
            field=models.ForeignKey(help_text=b'If location is mixed, such as &quot;Monday in the Mission, Thursday RM 104&quot; then select Other as location and fill in Other Location field.', to='courses.Room'),
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
            field=models.ManyToManyField(to='people.Profile', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='material',
            name='offering',
            field=models.ForeignKey(to='courses.Offering'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evalresponse',
            name='offering',
            field=models.ForeignKey(verbose_name=b'Offering', to='courses.Offering', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evalresponse',
            name='q_group',
            field=models.ForeignKey(verbose_name=b'In question set', to='courses.EvalQGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evalresponse',
            name='question',
            field=models.ForeignKey(to='courses.EvalQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evalresponse',
            name='semester',
            field=models.ForeignKey(to='courses.Semester'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evalquestion',
            name='semester_added',
            field=models.ForeignKey(to='courses.Semester'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evallog',
            name='offering',
            field=models.ForeignKey(blank=True, to='courses.Offering', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evallog',
            name='q_group',
            field=models.ForeignKey(verbose_name=b'Question Group', blank=True, to='courses.EvalQGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evallog',
            name='sem',
            field=models.ForeignKey(verbose_name=b'Semester', to='courses.Semester'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='evallog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='majors',
            field=models.ManyToManyField(to='courses.Major', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='programs',
            field=models.ManyToManyField(to='courses.Program', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='offering',
            field=models.ForeignKey(to='courses.Offering'),
            preserve_default=True,
        ),
    ]
