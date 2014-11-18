# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImporterCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('action', models.CharField(blank=True, max_length=2)),
                ('course_sec_id', models.CharField(blank=True, max_length=128)),
                ('course', models.CharField(blank=True, max_length=128)),
                ('section', models.CharField(blank=True, max_length=128)),
                ('sec_short_title', models.CharField(blank=True, max_length=128)),
                ('sec_desc', models.TextField(blank=True)),
                ('sec_start_date', models.CharField(blank=True, max_length=128)),
                ('sec_end_date', models.CharField(blank=True, max_length=128)),
                ('dept', models.CharField(blank=True, max_length=128)),
                ('sec_csxl', models.CharField(blank=True, max_length=128)),
                ('sec_term', models.CharField(blank=True, max_length=128)),
                ('short_title_formatted', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'db_table': 'importer_courses',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('due_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('long_title', models.CharField(max_length=100)),
                ('internal_title', models.CharField(max_length=16)),
                ('short_title_formatted', models.CharField(max_length=64)),
                ('units', models.IntegerField(null=True, blank=True, choices=[(1, '1'), (15, '1.5'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (99, 'var')])),
                ('course_type', models.IntegerField(null=True, blank=True, choices=[(1, 'Non-Graduate / General Courses'), (2, 'Required Courses'), (3, 'Background Courses'), (4, 'Advanced Reporting Courses'), (5, 'Skills Courses'), (6, 'Recommended Outside Classes')])),
                ('description', models.TextField(null=True, blank=True)),
                ('restrictions', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('day', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('obtain_at', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField(null=True, blank=True)),
                ('cost', models.DecimalField(null=True, blank=True, verbose_name='Approximate Cost', max_digits=8, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('course_sec_id', models.IntegerField(verbose_name='Section ID (from datatel)', unique=True)),
                ('section', models.CharField(null=True, blank=True, max_length=4, verbose_name='Section', choices=[('1', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('8', '08'), ('9', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('100', '100')])),
                ('title', models.CharField(null=True, blank=True, max_length=384, help_text='If present, overrides same field in Course model.')),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('start_time', models.TimeField(null=True, blank=True, help_text='Use military time, e.g. 08:30:00 for 8:30 am')),
                ('duration', models.FloatField(null=True, blank=True, help_text='Class meeting length. Enter as integers: For a 90 minute class enter 1.5')),
                ('location_other', models.CharField(blank=True, max_length=100)),
                ('grading', models.TextField(null=True, blank=True)),
                ('policies', models.TextField(null=True, blank=True)),
                ('fee', models.BooleanField(default=False, help_text='Fee required to take this course?')),
                ('enroll_lim', models.IntegerField(null=True, blank=True, verbose_name='Enrollment limit', help_text='Enrollment limit for this course (select nothing if there isn&apos;t one.)', choices=[('1', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('8', '08'), ('9', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('100', '100')])),
                ('description_override', models.TextField(null=True, blank=True, help_text='If present, overrides same field in Course model.')),
                ('restrictions_override', models.TextField(null=True, blank=True, help_text='If present, overrides same field in Course model.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(blank=True, verbose_name='Room Name', max_length=64, default='')),
                ('number', models.CharField(blank=True, verbose_name='Room Number', max_length=64, default='')),
                ('has_screen', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=96)),
                ('current', models.NullBooleanField(unique=True, help_text='Select &quot;Yes&quot; for the current semester, &quot;Unknown&quot; for all others. Ignore the &quot;No&quot; option. Only one semester may be marked current at a time.')),
                ('ord_by', models.IntegerField(null=True, blank=True)),
                ('live', models.BooleanField(default=False, help_text='When checked, this semester&apos;s schedule will appear on the public site.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
