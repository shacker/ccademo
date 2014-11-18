# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
from django.conf import settings
import people.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('dashboard', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImporterUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('action', models.CharField(blank=True, max_length=2)),
                ('person_id', models.IntegerField(null=True, blank=True)),
                ('section_id', models.IntegerField(null=True, blank=True)),
                ('first_name', models.CharField(blank=True, max_length=24)),
                ('last_name', models.CharField(blank=True, max_length=24)),
                ('email', models.CharField(blank=True, max_length=32)),
                ('photo_url', models.CharField(blank=True, max_length=140)),
                ('person_type', models.CharField(blank=True, max_length=12)),
            ],
            options={
                'db_table': 'importer_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('address_type', models.IntegerField(max_length=2, choices=[(1, 'Home'), (2, 'Work')])),
                ('street_1', models.CharField(null=True, blank=True, max_length=200)),
                ('street_2', models.CharField(null=True, blank=True, max_length=200)),
                ('street_3', models.CharField(null=True, blank=True, max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', localflavor.us.models.USStateField(null=True, blank=True, max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('state_other', models.CharField(null=True, blank=True, max_length=384, help_text='Useful for international addresses.')),
                ('postal_code', models.CharField(null=True, blank=True, max_length=50)),
                ('display', models.BooleanField(default=True, help_text='Display this address on my profile page')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_received', models.DateField(null=True, blank=True, help_text='Please enter dates in this format: 1986-09-13 for Sept. 13 1986.')),
                ('display', models.BooleanField(default=True, help_text='Display item on my public profile page')),
            ],
            options={
                'ordering': ['-date_received'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('description', models.CharField(null=True, blank=True, max_length=765)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'people_donation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('diploma', models.IntegerField(null=True, blank=True, max_length=3, choices=[(1, 'Bachelor of Arts'), (5, 'Bachelor of Science'), (6, 'Masters of Arts'), (8, 'Masters of Business Administration'), (7, 'Masters of Fine Arts'), (4, 'Masters of Journalism'), (2, 'Masters Of Science'), (9, 'Juris Doctorate'), (10, 'Medical Doctorate'), (3, 'Ph.D.')])),
                ('school', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.TextField(null=True, blank=True, help_text='Summary of education period.')),
                ('start_date', models.DateField(null=True, blank=True, help_text='Please enter dates in this format: 1986-09-13 for Sept. 13 1986.')),
                ('end_date', models.DateField(null=True, blank=True, help_text='Please enter dates in this format: 1986-09-13 for Sept. 13 1986.')),
                ('display', models.BooleanField(default=True, help_text='Display item on my public profile page')),
            ],
            options={
                'ordering': ['-start_date'],
                'verbose_name_plural': 'Education',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('experience_type', models.IntegerField(null=True, blank=True, max_length=3, choices=[(1, 'Full-Time Job'), (2, 'Part-Time Job'), (3, 'Paid internship'), (4, 'Unpaid internship'), (5, 'Volunteer'), (6, 'Other')])),
                ('title', models.CharField(null=True, blank=True, max_length=200, help_text='Title you held at this job or internship.')),
                ('description', models.TextField(null=True, blank=True, help_text='Summary of the experience.')),
                ('company', models.CharField(null=True, blank=True, max_length=200, help_text='Company or organization name.')),
                ('city', models.CharField(null=True, blank=True, max_length=200)),
                ('state', localflavor.us.models.USStateField(null=True, blank=True, max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('country', models.CharField(null=True, blank=True, max_length=200)),
                ('start_date', models.DateField(null=True, blank=True, help_text='Please enter dates in this format: 1986-09-13 for Sept. 13 1986.')),
                ('end_date', models.DateField(null=True, blank=True, help_text='Please enter dates in this format: 1986-09-13 for Sept. 13 1986.')),
                ('display', models.BooleanField(default=True, help_text='Display item on my public profile page')),
            ],
            options={
                'ordering': ['-start_date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('medium_id', models.IntegerField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=96)),
            ],
            options={
                'db_table': 'medium',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, primary_key=True)),
                ('person_id', models.IntegerField(null=True, blank=True, help_text='Datatel ID')),
                ('photo', easy_thumbnails.fields.ThumbnailerImageField(null=True, blank=True, upload_to=people.models.get_avatar_path)),
                ('datatel_avatar_url', models.CharField(null=True, blank=True, max_length=60, verbose_name='Datatel avatar URL')),
                ('suffix', models.IntegerField(null=True, blank=True, max_length=2, help_text='e.g. Dr., Phd.', choices=[(1, 'Ph.D'), (2, 'MD')])),
                ('salutation', models.IntegerField(null=True, blank=True, max_length=2, help_text='e.g. Mrs., Ms., Mr.', choices=[(1, 'Mr.'), (2, 'Mrs.'), (3, 'Ms.')])),
                ('middle_name', models.CharField(null=True, blank=True, max_length=50)),
                ('twitter', models.CharField(null=True, blank=True, max_length=64, help_text='Your twitter username')),
                ('facebook', models.CharField(null=True, blank=True, max_length=64, help_text='Your Facebook username')),
                ('title', models.CharField(null=True, blank=True, max_length=32)),
                ('about', models.TextField(null=True, blank=True, max_length=256, help_text='A few sentences about yourself - capsule biography. No HTML allowed.')),
                ('email2', models.EmailField(null=True, blank=True, max_length=75, verbose_name='Secondary Email')),
                ('home_phone1', models.CharField(null=True, blank=True, max_length=60, verbose_name='Home Phone')),
                ('biz_phone1', models.CharField(null=True, blank=True, max_length=60, verbose_name='Business Phone')),
                ('mobile_phone1', models.CharField(null=True, blank=True, max_length=60, verbose_name='Mobile Phone')),
                ('fax', models.CharField(null=True, blank=True, max_length=60)),
                ('allow_contact', models.BooleanField(default=True, help_text='Allow the public to contact you through the CCA Intranet.')),
                ('show_name', models.BooleanField(default=True, help_text='Not currently implemented, for future use.')),
                ('url_personal', models.URLField(null=True, blank=True, verbose_name='Personal website')),
                ('url_org', models.URLField(null=True, blank=True, verbose_name='Organization website')),
                ('accepted_terms', models.BooleanField(default=False, help_text='All users must accept our terms and conditions before doing anything on the site.')),
                ('email_on_follow', models.BooleanField(default=True, help_text='Receive email when someone follows you.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('profile', models.OneToOneField(serialize=False, to='people.Profile', primary_key=True)),
                ('office_num', models.CharField(null=True, blank=True, max_length=30, help_text='Room number')),
                ('extension', models.CharField(null=True, blank=True, max_length=30, help_text='UC Berkeley phone extension, e.g. 3-1234')),
                ('bio_short', models.TextField(help_text='Required for all instructors; used on index pages. Limited to around 175 words.')),
                ('bio_long', models.TextField(null=True, blank=True, help_text='Used on instructor detail pages.')),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructors',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('profile', models.OneToOneField(serialize=False, to='people.Profile', primary_key=True)),
                ('grad_year', models.IntegerField(null=True, verbose_name='Graduation year', max_length=4, choices=[(2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989'), (1988, '1988'), (1987, '1987'), (1986, '1986'), (1985, '1985'), (1984, '1984'), (1983, '1983'), (1982, '1982'), (1981, '1981'), (1980, '1980'), (1979, '1979'), (1978, '1978'), (1977, '1977'), (1976, '1976'), (1975, '1975'), (1974, '1974'), (1973, '1973'), (1972, '1972'), (1971, '1971'), (1970, '1970'), (1969, '1969'), (1968, '1968'), (1967, '1967'), (1966, '1966'), (1965, '1965'), (1964, '1964'), (1963, '1963'), (1962, '1962'), (1961, '1961'), (1960, '1960'), (1959, '1959'), (1958, '1958'), (1957, '1957'), (1956, '1956'), (1955, '1955'), (1954, '1954'), (1953, '1953'), (1952, '1952'), (1951, '1951'), (1950, '1950'), (1949, '1949'), (1948, '1948'), (1947, '1947'), (1946, '1946'), (1945, '1945'), (1944, '1944'), (1943, '1943'), (1942, '1942'), (1941, '1941'), (1940, '1940'), (1939, '1939'), (1938, '1938'), (1937, '1937'), (1936, '1936'), (1935, '1935'), (1934, '1934'), (1933, '1933'), (1932, '1932'), (1931, '1931'), (1930, '1930'), (1929, '1929'), (1928, '1928'), (1927, '1927'), (1926, '1926'), (1925, '1925'), (1924, '1924'), (1923, '1923'), (1922, '1922'), (1921, '1921'), (1920, '1920'), (1919, '1919'), (1918, '1918'), (1917, '1917'), (1916, '1916'), (1915, '1915'), (1914, '1914'), (1913, '1913'), (1912, '1912'), (1911, '1911'), (1910, '1910'), (1909, '1909'), (1908, '1908'), (1907, '1907'), (1906, '1906'), (1905, '1905'), (1904, '1904'), (1903, '1903'), (1902, '1902'), (1901, '1901'), (1900, '1900'), (0, '0')])),
                ('third_year', models.BooleanField(verbose_name='Is this student on the 3-year plan?', default=False)),
                ('j200_inst', models.CharField(null=True, blank=True, max_length=100, verbose_name='J200 Instructor', help_text='e.g. Gorney')),
                ('funding_amount', models.FloatField(null=True, blank=True, default=0)),
                ('enrollment_date', models.DateField(null=True, blank=True)),
                ('program_length', models.IntegerField(null=True, blank=True)),
                ('equipment_balance', models.FloatField(default=0.0)),
                ('visiting_scholar', models.BooleanField(default=False, help_text='Check box if this student is a visiting scholar.')),
                ('employer', models.CharField(null=True, blank=True, max_length=255)),
                ('specialty', models.CharField(null=True, blank=True, max_length=128, help_text='e.g. Sports')),
                ('medium', models.IntegerField(null=True, blank=True, max_length=4, choices=[(2, 'Broadcast'), (3, 'Documentary Film'), (4, 'New Media'), (5, 'Newspaper'), (6, 'Magazine'), (8, 'Private Investigating'), (9, 'Public Affairs/Relations'), (10, 'Teaching'), (11, 'Other (Journalism)'), (12, 'Other (Non-Journalism)'), (13, 'Wire Services'), (14, 'Photography'), (15, 'Book Author')])),
                ('prev_emp1', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Employer #1')),
                ('prev_emp2', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Employer #2')),
                ('prev_emp3', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Employer #3')),
                ('notes_exclude', models.BooleanField(verbose_name='Exclude notes', default=False, help_text='Please do NOT include my notes in the alumni newsletter.')),
                ('notes', models.TextField(null=True, blank=True, help_text="Tell us what you're up to, or add general notes on your life, whereabouts and recent projects.")),
                ('mod_date', models.DateField(auto_now=True)),
                ('pub_display', models.BooleanField(verbose_name='Display Option', default=True, help_text='If unchecked, record will be hidden even from other CCA alumni, faculty, students and staff.')),
                ('freelance', models.BooleanField(verbose_name='Freelancing?', default=False)),
                ('region', models.IntegerField(null=True, blank=True, max_length=4, choices=[(1, 'New England'), (2, 'East Coast'), (3, 'South'), (4, 'Midwest'), (5, 'Northwest'), (6, 'West Coast'), (7, 'Southwest'), (8, 'New York')])),
                ('prev_intern1', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Intership 1')),
                ('prev_intern2', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Intership 1')),
                ('prev_intern3', models.CharField(null=True, blank=True, max_length=384, verbose_name='Previous Intership 1')),
                ('first_job', models.CharField(null=True, blank=True, max_length=384, verbose_name='First job out of CCA')),
                ('books', models.TextField(null=True, blank=True)),
                ('deceased_notes', models.CharField(null=True, blank=True, max_length=255)),
                ('mia', models.BooleanField(default=False, help_text='Unable to contact this person, whereabouts unknown.')),
                ('mia_notes', models.TextField(null=True, blank=True)),
                ('interview', models.BooleanField(default=False, help_text='Has this person been interviewed [for xxx?]')),
                ('interview_year', models.IntegerField(default=0, choices=[(2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989'), (1988, '1988'), (1987, '1987'), (1986, '1986'), (1985, '1985'), (1984, '1984'), (1983, '1983'), (1982, '1982'), (1981, '1981'), (1980, '1980'), (1979, '1979'), (1978, '1978'), (1977, '1977'), (1976, '1976'), (1975, '1975'), (1974, '1974'), (1973, '1973'), (1972, '1972'), (1971, '1971'), (1970, '1970'), (1969, '1969'), (1968, '1968'), (1967, '1967'), (1966, '1966'), (1965, '1965'), (1964, '1964'), (1963, '1963'), (1962, '1962'), (1961, '1961'), (1960, '1960'), (1959, '1959'), (1958, '1958'), (1957, '1957'), (1956, '1956'), (1955, '1955'), (1954, '1954'), (1953, '1953'), (1952, '1952'), (1951, '1951'), (1950, '1950'), (1949, '1949'), (1948, '1948'), (1947, '1947'), (1946, '1946'), (1945, '1945'), (1944, '1944'), (1943, '1943'), (1942, '1942'), (1941, '1941'), (1940, '1940'), (1939, '1939'), (1938, '1938'), (1937, '1937'), (1936, '1936'), (1935, '1935'), (1934, '1934'), (1933, '1933'), (1932, '1932'), (1931, '1931'), (1930, '1930'), (1929, '1929'), (1928, '1928'), (1927, '1927'), (1926, '1926'), (1925, '1925'), (1924, '1924'), (1923, '1923'), (1922, '1922'), (1921, '1921'), (1920, '1920'), (1919, '1919'), (1918, '1918'), (1917, '1917'), (1916, '1916'), (1915, '1915'), (1914, '1914'), (1913, '1913'), (1912, '1912'), (1911, '1911'), (1910, '1910'), (1909, '1909'), (1908, '1908'), (1907, '1907'), (1906, '1906'), (1905, '1905'), (1904, '1904'), (1903, '1903'), (1902, '1902'), (1901, '1901'), (1900, '1900'), (0, '0')])),
                ('interview_notes', models.TextField(null=True, blank=True)),
                ('agents_year', models.IntegerField(null=True, blank=True, help_text='Not sure what this field is for?', default=0, choices=[(2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989'), (1988, '1988'), (1987, '1987'), (1986, '1986'), (1985, '1985'), (1984, '1984'), (1983, '1983'), (1982, '1982'), (1981, '1981'), (1980, '1980'), (1979, '1979'), (1978, '1978'), (1977, '1977'), (1976, '1976'), (1975, '1975'), (1974, '1974'), (1973, '1973'), (1972, '1972'), (1971, '1971'), (1970, '1970'), (1969, '1969'), (1968, '1968'), (1967, '1967'), (1966, '1966'), (1965, '1965'), (1964, '1964'), (1963, '1963'), (1962, '1962'), (1961, '1961'), (1960, '1960'), (1959, '1959'), (1958, '1958'), (1957, '1957'), (1956, '1956'), (1955, '1955'), (1954, '1954'), (1953, '1953'), (1952, '1952'), (1951, '1951'), (1950, '1950'), (1949, '1949'), (1948, '1948'), (1947, '1947'), (1946, '1946'), (1945, '1945'), (1944, '1944'), (1943, '1943'), (1942, '1942'), (1941, '1941'), (1940, '1940'), (1939, '1939'), (1938, '1938'), (1937, '1937'), (1936, '1936'), (1935, '1935'), (1934, '1934'), (1933, '1933'), (1932, '1932'), (1931, '1931'), (1930, '1930'), (1929, '1929'), (1928, '1928'), (1927, '1927'), (1926, '1926'), (1925, '1925'), (1924, '1924'), (1923, '1923'), (1922, '1922'), (1921, '1921'), (1920, '1920'), (1919, '1919'), (1918, '1918'), (1917, '1917'), (1916, '1916'), (1915, '1915'), (1914, '1914'), (1913, '1913'), (1912, '1912'), (1911, '1911'), (1910, '1910'), (1909, '1909'), (1908, '1908'), (1907, '1907'), (1906, '1906'), (1905, '1905'), (1904, '1904'), (1903, '1903'), (1902, '1902'), (1901, '1901'), (1900, '1900'), (0, '0')])),
                ('agents_notes', models.TextField(null=True, blank=True, help_text='Not sure what this field is for?')),
                ('event_attend_notes', models.TextField(null=True, blank=True)),
                ('famous_notes', models.TextField(null=True, blank=True)),
                ('volunteer_speak', models.BooleanField(default=False, help_text="I'm happy to speak with current students about my career path, what it's like to work at my news outlet (or as a freelancer) and what sort of internship opportunities exist in my workplace.")),
                ('volunteer_committee', models.BooleanField(default=False, help_text="I'd like to volunteer to get more involved with planning events and alumni outreach. I might even have suggestions for events in my area.")),
                ('volunteer_interview', models.BooleanField(default=False, help_text="I'd like to interview students in my area to help with the admissions process.")),
                ('volunteer_mentor', models.BooleanField(default=False, help_text="I'd like to be matched with a student during the school year to provide additional career guidance.")),
                ('volunteer_agent', models.BooleanField(default=False, help_text="I'd like to be a Class Agent and serve as a liason between the Alumni Board and my graduating classes.")),
                ('maillist_class', models.BooleanField(default=False, help_text='Please add me to my class email list.')),
                ('no_maillists', models.BooleanField(default=False, help_text='I do NOT want to receive any email from the journalism school. Please make sure I am NOT on any of the mailing lists.')),
                ('no_reminder', models.BooleanField(default=False, help_text='I would like to opt-out from the twice yearly reminder email.')),
                ('suggestions', models.TextField(null=True, blank=True, help_text="Do you have suggestions for us about what you'd like to get out of the CCA Alumni Organization? If so, please write us a note and we'll try to incorporate your idea.")),
                ('committee_notes', models.TextField(null=True, blank=True)),
                ('inactive', models.BooleanField(default=False)),
                ('revision', models.IntegerField(null=True, blank=True, help_text='This field should increment up when record is updated.')),
            ],
            options={
                'verbose_name': 'Alumni',
                'verbose_name_plural': 'Alumni',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('summary', models.TextField()),
                ('display', models.BooleanField(default=True, help_text='Display item on my public profile page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('profile', models.OneToOneField(serialize=False, to='people.Profile', primary_key=True)),
                ('office_num', models.CharField(null=True, blank=True, max_length=30, verbose_name='Office', help_text='Room number')),
                ('extension', models.CharField(null=True, blank=True, max_length=30, help_text='UC Berkeley Phone Extension #-####')),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile', models.OneToOneField(serialize=False, to='people.Profile', primary_key=True)),
                ('grad_year', models.IntegerField(null=True, blank=True, max_length=4, verbose_name='Graduation year', choices=[(2013, '2013'), (2012, '2012'), (2011, '2011'), (2010, '2010'), (2009, '2009'), (2008, '2008'), (2007, '2007'), (2006, '2006'), (2005, '2005'), (2004, '2004'), (2003, '2003'), (2002, '2002'), (2001, '2001'), (2000, '2000'), (1999, '1999'), (1998, '1998'), (1997, '1997'), (1996, '1996'), (1995, '1995'), (1994, '1994'), (1993, '1993'), (1992, '1992'), (1991, '1991'), (1990, '1990'), (1989, '1989'), (1988, '1988'), (1987, '1987'), (1986, '1986'), (1985, '1985'), (1984, '1984'), (1983, '1983'), (1982, '1982'), (1981, '1981'), (1980, '1980'), (1979, '1979'), (1978, '1978'), (1977, '1977'), (1976, '1976'), (1975, '1975'), (1974, '1974'), (1973, '1973'), (1972, '1972'), (1971, '1971'), (1970, '1970'), (1969, '1969'), (1968, '1968'), (1967, '1967'), (1966, '1966'), (1965, '1965'), (1964, '1964'), (1963, '1963'), (1962, '1962'), (1961, '1961'), (1960, '1960'), (1959, '1959'), (1958, '1958'), (1957, '1957'), (1956, '1956'), (1955, '1955'), (1954, '1954'), (1953, '1953'), (1952, '1952'), (1951, '1951'), (1950, '1950'), (1949, '1949'), (1948, '1948'), (1947, '1947'), (1946, '1946'), (1945, '1945'), (1944, '1944'), (1943, '1943'), (1942, '1942'), (1941, '1941'), (1940, '1940'), (1939, '1939'), (1938, '1938'), (1937, '1937'), (1936, '1936'), (1935, '1935'), (1934, '1934'), (1933, '1933'), (1932, '1932'), (1931, '1931'), (1930, '1930'), (1929, '1929'), (1928, '1928'), (1927, '1927'), (1926, '1926'), (1925, '1925'), (1924, '1924'), (1923, '1923'), (1922, '1922'), (1921, '1921'), (1920, '1920'), (1919, '1919'), (1918, '1918'), (1917, '1917'), (1916, '1916'), (1915, '1915'), (1914, '1914'), (1913, '1913'), (1912, '1912'), (1911, '1911'), (1910, '1910'), (1909, '1909'), (1908, '1908'), (1907, '1907'), (1906, '1906'), (1905, '1905'), (1904, '1904'), (1903, '1903'), (1902, '1902'), (1901, '1901'), (1900, '1900'), (0, '0')])),
                ('funding_amount', models.FloatField(null=True, blank=True, default=0)),
                ('enrollment_date', models.DateField(null=True, blank=True)),
                ('program_length', models.IntegerField(null=True, blank=True)),
                ('visiting_scholar', models.BooleanField(default=False, help_text='Check box if this student is a visiting scholar.')),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reference',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='dashboard_widgets',
            field=models.ManyToManyField(null=True, blank=True, to='dashboard.CCAWidget', through='dashboard.UserWidget', help_text='This users set of Dashboard Widgets'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='followees',
            field=models.ManyToManyField(null=True, blank=True, to='people.Profile', related_name='followers', help_text='People this person is following.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='planned_classes',
            field=models.ManyToManyField(null=True, blank=True, to='courses.Builder', related_name='planned_classes', help_text='Classes this user intends to take'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='donation',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='award',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.ForeignKey(to='people.Profile'),
            preserve_default=True,
        ),
    ]
