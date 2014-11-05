import os
import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.conf import settings
from fabric.operations import local
from courses.models import ImporterCourses, Room, Program, Semester, Course, Offering


'''
0) Drop and recreate import_courses table
1) Import entire CSV into import_courses
2) Loop through UNIQUE importer_courses and create Course and CourseOffering objects as needed
'''

import_file = os.path.join(settings.IMPORTER_DATA_DIR, 'C56.MOODLE.SECTIONS.csv')
schema_file = os.path.join(settings.BASE_DIR, 'apps', 'base', 'management', 'commands', 'importer_courses.sql')
import_db = settings.DATABASES['default']['NAME']


class Command(BaseCommand):
    help = "Drops old course import temp table, recreate, populate from CSV data, create corresponding course records."

    def handle(self, *args, **options):

        local("psql -d {db} -c 'DROP TABLE IF EXISTS importer_courses'".format(db=import_db))
        local("psql -d {db} -f {schema_file}".format(db=import_db, schema_file=schema_file))
        local('psql -d {db} -c "set client_encoding to \'LATIN1\'; COPY importer_courses (action,course_sec_id,course,section,sec_short_title,sec_desc,sec_start_date,sec_end_date, dept, sec_csxl, sec_term, short_title_formatted) FROM \'{import_file}\' WITH DELIMITER \',\' CSV HEADER"'.format(db=import_db, import_file=import_file))

        temp_courses = ImporterCourses.objects.all().distinct('course_sec_id')
        for tc in temp_courses:
            print("row ", tc.id)
            if tc.action == "A":  # Only act on ADDs for now
                # We need both a Course and an Offering. Check to see whether they exist before creating

                try:
                    course = Course.objects.get(internal_title=tc.course)
                    print(course, " already exists, skipping import.")
                except:
                    course = Course.objects.create(
                        long_title = tc.sec_short_title,
                        internal_title = tc.course,
                        short_title_formatted = tc.short_title_formatted,
                        description = tc.sec_desc,
                    )
                    print("Created course ", course)

                # What program is this course offered under? Create program if needed
                try:
                    prog = Program.objects.get(name=tc.dept)
                except:
                    prog = Program.objects.create(
                        name = tc.dept,
                        slug = tc.dept,
                    )
                print("Program is ", prog)

                # Add current course to selected program
                course.programs.add(prog)

                # Get or create Semester and Room objects
                # created is True if new object was created
                semester, created = Semester.objects.get_or_create(name=tc.sec_term,)
                room, created = Room.objects.get_or_create(number="100",)

                # TODO - change others to get_or_create

                # Set up a course offering for this course
                try:
                    offering = Offering.objects.get(course_sec_id = tc.course_sec_id)
                    print("Course offering ", offering, " already exists, skipping.")
                except:
                    offering = Offering.objects.create(
                        course = course,
                        course_sec_id = tc.course_sec_id,
                        section = tc.section,
                        sec_term = semester,
                        start_date = datetime.datetime.strptime(tc.sec_start_date, "%m/%d/%Y"),
                        end_date = datetime.datetime.strptime(tc.sec_end_date, "%m/%d/%Y"),
                        location = room,
                    )
                    print("Created offering ", offering)
                print




