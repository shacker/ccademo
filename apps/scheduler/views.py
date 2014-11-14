import json
import random
from time import strftime
from datetime import datetime, timedelta
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from courses.models import Offering
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from scheduler.utils import generate_date_strings


def scheduler(request):
    """
    Show the current user's schedule of courses
    """

    myclasses = Offering.objects.filter(students__in=(request.user,))

    return render_to_response(
        'scheduler/show.html',
        locals(),
        context_instance=RequestContext(request)
        )



def scheduler_json(request):

    '''
    Output user's ScheduleBuilder classes as JSON for use by jQuery FullCalendar.
    Final output needs to look like:

    [
        {
        "start": "2014-11-14 13:00:25.015320",
        "end": "2014-11-14 14:30:25.015320",
        "title": "L: Reading Franz Kafka"
        },
        {
        "start": "2014-11-13 09:00:25.018352",
        "end": "2014-11-13 10:30:25.018352",
        "title": "CP2: Engage: Public Space"
        }
    ]
    '''

    offerings = Offering.objects.filter(students__in=(request.user,))
    pallette = ['#5e9964', '#99368c', '#446fba', '#5fba39', '#432919', '#302043', '#9d122c']
    data = []

    for o in offerings:
        # This offering could happen on multiple days of the week.
        # Set event color per class, not event, so matched class events have matching colors.
        # Don't reuse colors - grab last color from list and remove.
        colorval = pallette.pop()

        for day_of_week in o.days_of_week.all():
            startstop = generate_date_strings(day_of_week, o.start_time, o.duration)

            # Stick the offering details into a serializable dictionary
            offering = {}
            offering['title'] = o.display_name()
            offering['start'] = str(startstop['start_date_time'])
            offering['end'] = str(startstop['end_date_time'])
            offering['url'] = reverse('offering_detail', kwargs={'course_sec_id': o.course_sec_id,})
            offering['color'] = colorval

            data.append(offering)

    return HttpResponse(
        json.dumps(data), content_type='application/json'
     )


def add_course_to_schedule(request,offering_id):
    '''
    Add the selected course to the current user's schedule.
    This view only invoked via ajax, never directly.
    We only need to return a 200, not a render_to_response.
    '''

    profile = request.user.profile
    offering = get_object_or_404(Offering, id=offering_id)

    if request.method == "POST":
        # Skipping the usual form validation since there's nothing but a button to click
        # and it's harmless to add classes to your own schedule.
        offering.students.add(profile)
        messages.success(request, "Course added to your ScheduleBuilder")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def remove_course_from_schedule(request,offering_id):
    '''
    Remove the selected course from the current user's schedule
    '''

    user = request.user
    offering = get_object_or_404(Offering, id=offering_id)

    offering.students.remove(request.user)
    messages.success(request, "Course removed from your schedule.")
    return HttpResponseRedirect(reverse('scheduler'))