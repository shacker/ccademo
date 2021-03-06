from django.conf.urls import patterns, include, url
from courses.models import *

# Program/courses URLs
urlpatterns = patterns('courses.views',

    # Course schedule and its printable version all use the same view, and can optionally take a "sem" (semester) argument.
    url(r'^schedule/sem/(?P<sem_id>[\d]+)/$', 'offerings_schedule', name="courses_schedule_sem"),
    url(r'^descriptions/sem/(?P<sem_id>[\d]+)/$', 'offerings_schedule', {'printable': True}, name="courses_descriptions_sem"),
    url(r'^schedule/$', 'offerings_schedule', name="offerings_schedule"),
    url(r'^descriptions/$', 'offerings_schedule', {'printable': True}, name="courses_descriptions"),
    url(r'^programs/(?P<slug>[\w-]+)$', 'programs_detail', name="programs_detail"),
    url(r'^programs/$', 'programs_list', name="programs_list"),

    url(r'^course/(?P<internal_title>[\w-]+)/$', 'course_detail',  name='course_detail'),

    # Course offering subsections
    url(r'^offering/(?P<course_sec_id>[\d]+)$', 'offering_detail', name="offering_detail"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/announcements$', 'offering_announcements', name="offering_announcements"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/contact$', 'offering_contact', name="offering_contact"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/policies$', 'offering_policies', name="offering_policies"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/assignments$', 'offering_assignments', name="offering_assignments"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/participants$', 'offering_participants', name="offering_participants"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/materials$', 'offering_materials', name="offering_materials"),
    url(r'^offering/(?P<course_sec_id>[\d]+)/library$', 'offering_library', name="offering_library"),

    url(r'^material/(?P<material_id>[\d]+)$', 'offering_material_detail', name="offering_material_detail"),
    url(r'^assignment/(?P<assign_id>[\d]+)$', 'offering_assignment_detail', name="offering_assignment_detail"),
)

