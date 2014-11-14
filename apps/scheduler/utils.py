from time import strftime
from datetime import datetime, timedelta, date
from django.core.urlresolvers import reverse


def generate_date_strings(day_of_week, start_time, duration):
    '''
    Given a day of week, start time and duration, returns
    a dictionary of actual start_time and end_time for the offering.
    Designed to be used to generate JSON data for the ScheduleBuilder.

    Important: We don't try to capture the actual start_date of the offering
    because we need to show all subscribed classes on the same week view
    of a calendar, while these might overlap across weeks so that some are
    invisible. Instead, we just pretend they're all starting today, and
    let the FullCalendar default to starting today as well.
    '''

    # Stupid python doesn't have a `case` statement
    if day_of_week.day == "Monday":
        date_diff = 0

    elif day_of_week.day == "Tuesday":
        date_diff = 1

    elif day_of_week.day == "Wednesday":
        date_diff = 2

    elif day_of_week.day == "Thursday":
        date_diff = 3

    elif day_of_week.day == "Friday":
        date_diff = 4

    else:
        # If no day of week is available we can't continue
        return False

    # We need to start with the Monday of the current week.
    today = datetime.today()
    today = today - timedelta(days=today.weekday())

    # Assuming we start the week on Monday, create a newdate,
    # adding the day of week offset as delta
    newdate = today + timedelta(days=date_diff)

    # Now swap in the actual course start time
    newdate_start = newdate.replace(hour=start_time.hour, minute=start_time.minute)

    # And add the duration to the hours to get an end date
    newdate_end = newdate_start + timedelta(hours=duration)

    return {
        'start_date_time': newdate_start,
        'end_date_time': newdate_end
        }