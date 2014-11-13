import os
import datetime
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.conf import settings
from courses.models import ImporterCourses, Room, Days, Program, Semester, Course, Offering


'''
Generate fake meeting times for Offerings
'''


class Command(BaseCommand):
    help = "Generate fake meeting times for Offerings"

    def handle(self, *args, **options):

        dayset = Days.objects.all()
        lengths = [1.0, 1.5, 2.0, 2.5, 3.0]
        times = [9, 10, 11, 12, 13, 14, 15, 16]

        offerings = Offering.objects.all()
        for o in offerings:
            print(o.id)

            daychoice = random.choice(dayset)
            timechoice = random.choice(times)
            durationchoice = random.choice(lengths)

            o.days_of_week.add(daychoice)
            o.start_time = "{start}:00".format(start=timechoice)
            o.duration = durationchoice
            o.save()


            print("{day}, {time}, {hours} hours".format(day=daychoice, time=timechoice, hours=durationchoice))
            print("=======")

