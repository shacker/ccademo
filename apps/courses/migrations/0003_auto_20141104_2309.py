# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141104_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImporterCourses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=2, blank=True)),
                ('course_sec_id', models.CharField(max_length=128, blank=True)),
                ('course', models.CharField(max_length=128, blank=True)),
                ('section', models.CharField(max_length=128, blank=True)),
                ('sec_short_title', models.CharField(max_length=128, blank=True)),
                ('sec_desc', models.TextField(blank=True)),
                ('sec_start_date', models.CharField(max_length=128, blank=True)),
                ('sec_end_date', models.CharField(max_length=128, blank=True)),
                ('dept', models.CharField(max_length=128, blank=True)),
                ('sec_csxl', models.CharField(max_length=128, blank=True)),
                ('sec_term', models.CharField(max_length=128, blank=True)),
                ('short_title_formatted', models.CharField(max_length=128, blank=True)),
            ],
            options={
                'db_table': 'importer_courses',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='course',
            name='section',
        ),
        migrations.AlterField(
            model_name='offering',
            name='enroll_lim',
            field=models.IntegerField(blank=True, help_text=b'Enrollment limit for this course (select nothing if there isn&apos;t one.)', null=True, verbose_name=b'Enrollment limit', choices=[(1, b'01'), (2, b'02'), (3, b'03'), (4, b'04'), (5, b'05'), (6, b'06'), (7, b'07'), (8, b'08'), (9, b'09'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21'), (22, b'22'), (23, b'23'), (24, b'24'), (25, b'25'), (26, b'26'), (27, b'27'), (28, b'28'), (29, b'29'), (30, b'30'), (31, b'31'), (32, b'32'), (33, b'33'), (34, b'34'), (35, b'35'), (36, b'36'), (37, b'37'), (38, b'38'), (39, b'39'), (40, b'40'), (41, b'41'), (42, b'42'), (43, b'43'), (44, b'44'), (45, b'45'), (46, b'46'), (47, b'47'), (48, b'48'), (49, b'49'), (50, b'50'), (51, b'51'), (52, b'52'), (53, b'53'), (54, b'54'), (55, b'55'), (56, b'56'), (57, b'57'), (58, b'58'), (59, b'59'), (60, b'60'), (61, b'61'), (62, b'62'), (63, b'63'), (64, b'64'), (65, b'65'), (66, b'66'), (67, b'67'), (68, b'68'), (69, b'69'), (70, b'70'), (71, b'71'), (72, b'72'), (73, b'73'), (74, b'74'), (75, b'75'), (76, b'76'), (77, b'77'), (78, b'78'), (79, b'79'), (80, b'80'), (81, b'81'), (82, b'82'), (83, b'83'), (84, b'84'), (85, b'85'), (86, b'86'), (87, b'87'), (88, b'88'), (89, b'89'), (90, b'90'), (91, b'91'), (92, b'92'), (93, b'93'), (94, b'94'), (95, b'95'), (96, b'96'), (97, b'97'), (98, b'98'), (99, b'99'), (100, b'100')]),
            preserve_default=True,
        ),
    ]
