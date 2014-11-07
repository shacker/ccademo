import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group
from django.conf import settings
from fabric.operations import local
from people.models import ImporterUsers, Profile, Staff, Student, Instructor, Alumni
from base.utils import generate_random_username, ldap_get_by_id


'''
0) Drop and recreate import_users table
1) Import entire CSV into import_users
2) Loop through UNIQUE importer_users and create User and profile objects as needed

DROP TABLE IF EXISTS importer_users
COPY importer_users (action,person_id,section_id,first_name,last_name,email,photo_url,person_type) FROM '/Users/shacker/dev/ccademo/data/enroldata/C56.MOODLE.STUFAC.EXP-short.csv' WITH DELIMITER ',' CSV HEADER;
'''

import_file = os.path.join(settings.IMPORTER_DATA_DIR, 'C56.MOODLE.STUFAC.EXP.csv')
schema_file = os.path.join(settings.BASE_DIR, 'apps', 'base', 'management', 'commands', 'importer_users.sql')
import_db = settings.DATABASES['default']['NAME']

student_group = Group.objects.get(name='Students')
faculty_group = Group.objects.get(name='Faculty')


class Command(BaseCommand):
    help = "Drops old user import temp table, recreate, populate from CSV data, create corresponding profile records."

    def handle(self, *args, **options):

        local("psql -d {db} -c 'DROP TABLE IF EXISTS importer_users'".format(db=import_db))
        local("psql -d {db} -f {schema_file}".format(db=import_db, schema_file=schema_file))
        local('psql -d {db} -c "COPY importer_users (action,person_id,section_id,first_name,last_name,email,photo_url,person_type) FROM \'{import_file}\' WITH DELIMITER \',\' CSV HEADER"'.format(db=import_db, import_file=import_file))

        # Right now we are just making sure we have correct users and profile records,
        # NOT processing enrolments.
        tempusers = ImporterUsers.objects.all().distinct('person_id')
        for tu in tempusers:
            # See if they have a profile with matching person_id
            # If not, create a User object for the (which will generate a vanilla Profile)
            # Then manually create a person type profile (Staff, Student) for them as well
            try:
                p = Profile.objects.get(person_id=tu.person_id)
                print("Profile for {user} exists. Skipping.".format(user=p.user))
            except:
                # Some records have empty fields
                if not tu.email:
                    tu.email = 'temp@example.com'
                if not tu.first_name:
                    tu.first_name = "Unknown"
                if not tu.last_name:
                    tu.last_name = "Unknown"

                # If we can't get a username from LDAP, generate a fake one
                # Reinstate later if we go forward
                # try:
                #     print tu.ccaEmployeeNumber
                #     results = ldap_get_by_id(tu.ccaEmployeeNumber)
                #     print(results)
                #     print
                #     username = results['uid']
                # except:
                #     username=generate_random_username(),
                #     print("Not found in ldap - rand username is {user}".format(user=username))

                try:
                    # We don't have usernames in moodle data, fake it with first part of email for now
                    username = tu.email.split('@')[0]
                except:
                    username = generate_random_username()

                # Make sure we don't already have this username (e.g. repeated use of "temp")
                if username == "temp":
                    username = generate_random_username()

                user = User.objects.create(
                    username=username,
                    first_name=tu.first_name,
                    last_name=tu.last_name,
                    email=tu.email,
                    )
                user.set_unusable_password()

                # Get a handle on the newly created Profile
                p = Profile.objects.get(user=user)
                p.person_id = tu.person_id
                p.datatel_avatar_url = tu.photo_url
                p.save()

                print("Created user {user}".format(user=p.get_display_name()))

                # Create corresponding Student profile and add them to group
                # TODO: Do similar for other group types
                if tu.person_type == 'student':
                    Student.objects.create(profile=p)
                    student_group.user_set.add(user)

                if tu.person_type == 'faculty':
                    Instructor.objects.create(profile=p)
                    faculty_group.user_set.add(user)

