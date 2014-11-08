# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_squashed_0012_auto_20141105_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.IntegerField(null=True, choices=[(1, 'Non-Graduate / General Courses'), (2, 'Required Courses'), (3, 'Background Courses'), (4, 'Advanced Reporting Courses'), (5, 'Skills Courses'), (6, 'Recommended Outside Classes')], blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='units',
            field=models.IntegerField(null=True, choices=[(1, '1'), (15, '1.5'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (99, 'var')], blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='material',
            name='cost',
            field=models.DecimalField(null=True, verbose_name='Approximate Cost', decimal_places=2, max_digits=8, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='course_sec_id',
            field=models.IntegerField(verbose_name='Section ID (from datatel)', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='description_override',
            field=models.TextField(null=True, help_text='If present, overrides same field in Course model.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='enroll_lim',
            field=models.IntegerField(null=True, choices=[('1', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('8', '08'), ('9', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('100', '100')], help_text='Enrollment limit for this course (select nothing if there isn&apos;t one.)', verbose_name='Enrollment limit', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='fee',
            field=models.BooleanField(default=False, help_text='Fee required to take this course?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='location',
            field=models.ForeignKey(to='courses.Room', help_text='If location is mixed, such as &quot;Monday in the Mission, Thursday RM 104&quot; then select Other as location and fill in Other Location field.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='restrictions_override',
            field=models.TextField(null=True, help_text='If present, overrides same field in Course model.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='section',
            field=models.CharField(null=True, choices=[('1', '01'), ('2', '02'), ('3', '03'), ('4', '04'), ('5', '05'), ('6', '06'), ('7', '07'), ('8', '08'), ('9', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'), ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'), ('59', '59'), ('60', '60'), ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'), ('69', '69'), ('70', '70'), ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'), ('79', '79'), ('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'), ('99', '99'), ('100', '100')], max_length=4, verbose_name='Section', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='offering',
            name='title',
            field=models.CharField(null=True, help_text='If present, overrides same field in Course model.', max_length=384, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='', verbose_name='Room Name', max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(default='', verbose_name='Room Number', max_length=64, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='semester',
            name='current',
            field=models.NullBooleanField(help_text='Select &quot;Yes&quot; for the current semester, &quot;Unknown&quot; for all others. Ignore the &quot;No&quot; option. Only one semester may be marked current at a time.', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='semester',
            name='live',
            field=models.BooleanField(default=False, help_text='When checked, this semester&apos;s schedule will appear on the public site.'),
            preserve_default=True,
        ),
    ]
