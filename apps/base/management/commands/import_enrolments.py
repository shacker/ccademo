import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.conf import settings
from fabric.operations import local
from people.models import ImporterUsers, Profile, Staff, Student, Instructor, Alumni
from courses.models import Offering
from base.utils import generate_random_username, ldap_get_by_id


'''
Run AFTER users and courses are imported. Process enrolment actions in STUFAC temp table
'''




class Command(BaseCommand):
    help = "Drops old user import temp table, recreate, populate from CSV data, create corresponding profile records."

    def handle(self, *args, **options):

        tempusers = ImporterUsers.objects.all().distinct('person_id')
        for tu in tempusers:

            try:
                profile = Profile.objects.get(person_id=tu.person_id)
            except:
                profile = None

            try:
                offering = Offering.objects.get(course_sec_id=tu.section_id)
            except:
                offering = None

            if profile and offering:
                # Process adds
                if tu.action == "A":
                    if tu.person_type == 'student':
                        offering.students.add(profile)
                        print("Added student {profile} to offering {offering}".format(profile=profile, offering=offering))

                    if tu.person_type == 'faculty':
                        instructor = Instructor.objects.get(profile=profile)
                        offering.instructors.add(instructor)
                        print("Added instructor {instructor} to offering {offering}".format(instructor=instructor, offering=offering))


                # Process drops
                if tu.action == "D":

                    if tu.person_type == 'student':
                        offering.students.remove(profile)
                        print("Removed student {profile} from offering {offering}".format(profile=profile, offering=offering))


                    if tu.person_type == 'faculty':
                        instructor = Instructor.objects.get(profile=profile)
                        offering.instructors.remove(instructor)
                        print("Removed instructor {instructor} from offering {offering}".format(instructor=instructor, offering=offering))


