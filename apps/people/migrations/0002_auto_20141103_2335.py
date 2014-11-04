# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.us.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImporterUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=2, blank=True)),
                ('person_id', models.IntegerField(null=True, blank=True)),
                ('section_id', models.IntegerField(null=True, blank=True)),
                ('first_name', models.CharField(max_length=24, blank=True)),
                ('last_name', models.CharField(max_length=24, blank=True)),
                ('email', models.CharField(max_length=32, blank=True)),
                ('photo_url', models.CharField(max_length=140, blank=True)),
                ('person_type', models.CharField(max_length=12, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_type', models.IntegerField(max_length=2, choices=[(1, b'Home'), (2, b'Work')])),
                ('street_1', models.CharField(max_length=200, null=True, blank=True)),
                ('street_2', models.CharField(max_length=200, null=True, blank=True)),
                ('street_3', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('state_other', models.CharField(help_text=b'Useful for international addresses.', max_length=384, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=50, null=True, blank=True)),
                ('display', models.BooleanField(default=True, help_text=b'Display this address on my profile page')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_received', models.DateField(help_text=b'Please enter dates in this format: 1986-09-13 for Sept. 13 1986.', null=True, blank=True)),
                ('display', models.BooleanField(default=True, help_text=b'Display item on my public profile page')),
            ],
            options={
                'ordering': ['-date_received'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=765, null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diploma', models.IntegerField(blank=True, max_length=3, null=True, choices=[(1, b'Bachelor of Arts'), (5, b'Bachelor of Science'), (6, b'Masters of Arts'), (8, b'Masters of Business Administration'), (7, b'Masters of Fine Arts'), (4, b'Masters of Journalism'), (2, b'Masters Of Science'), (9, b'Juris Doctorate'), (10, b'Medical Doctorate'), (3, b'Ph.D.')])),
                ('school', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField(help_text=b'Summary of education period.', null=True, blank=True)),
                ('start_date', models.DateField(help_text=b'Please enter dates in this format: 1986-09-13 for Sept. 13 1986.', null=True, blank=True)),
                ('end_date', models.DateField(help_text=b'Please enter dates in this format: 1986-09-13 for Sept. 13 1986.', null=True, blank=True)),
                ('display', models.BooleanField(default=True, help_text=b'Display item on my public profile page')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience_type', models.IntegerField(blank=True, max_length=3, null=True, choices=[(1, b'Full-Time Job'), (2, b'Part-Time Job'), (3, b'Paid internship'), (4, b'Unpaid internship'), (5, b'Volunteer'), (6, b'Other')])),
                ('title', models.CharField(help_text=b'Title you held at this job or internship.', max_length=200, null=True, blank=True)),
                ('description', models.TextField(help_text=b'Summary of the experience.', null=True, blank=True)),
                ('company', models.CharField(help_text=b'Company or organization name.', max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200, null=True, blank=True)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2, null=True, choices=[(b'AL', b'Alabama'), (b'AK', b'Alaska'), (b'AS', b'American Samoa'), (b'AZ', b'Arizona'), (b'AR', b'Arkansas'), (b'AA', b'Armed Forces Americas'), (b'AE', b'Armed Forces Europe'), (b'AP', b'Armed Forces Pacific'), (b'CA', b'California'), (b'CO', b'Colorado'), (b'CT', b'Connecticut'), (b'DE', b'Delaware'), (b'DC', b'District of Columbia'), (b'FL', b'Florida'), (b'GA', b'Georgia'), (b'GU', b'Guam'), (b'HI', b'Hawaii'), (b'ID', b'Idaho'), (b'IL', b'Illinois'), (b'IN', b'Indiana'), (b'IA', b'Iowa'), (b'KS', b'Kansas'), (b'KY', b'Kentucky'), (b'LA', b'Louisiana'), (b'ME', b'Maine'), (b'MD', b'Maryland'), (b'MA', b'Massachusetts'), (b'MI', b'Michigan'), (b'MN', b'Minnesota'), (b'MS', b'Mississippi'), (b'MO', b'Missouri'), (b'MT', b'Montana'), (b'NE', b'Nebraska'), (b'NV', b'Nevada'), (b'NH', b'New Hampshire'), (b'NJ', b'New Jersey'), (b'NM', b'New Mexico'), (b'NY', b'New York'), (b'NC', b'North Carolina'), (b'ND', b'North Dakota'), (b'MP', b'Northern Mariana Islands'), (b'OH', b'Ohio'), (b'OK', b'Oklahoma'), (b'OR', b'Oregon'), (b'PA', b'Pennsylvania'), (b'PR', b'Puerto Rico'), (b'RI', b'Rhode Island'), (b'SC', b'South Carolina'), (b'SD', b'South Dakota'), (b'TN', b'Tennessee'), (b'TX', b'Texas'), (b'UT', b'Utah'), (b'VT', b'Vermont'), (b'VI', b'Virgin Islands'), (b'VA', b'Virginia'), (b'WA', b'Washington'), (b'WV', b'West Virginia'), (b'WI', b'Wisconsin'), (b'WY', b'Wyoming')])),
                ('country', models.CharField(max_length=200, null=True, blank=True)),
                ('start_date', models.DateField(help_text=b'Please enter dates in this format: 1986-09-13 for Sept. 13 1986.', null=True, blank=True)),
                ('end_date', models.DateField(help_text=b'Please enter dates in this format: 1986-09-13 for Sept. 13 1986.', null=True, blank=True)),
                ('display', models.BooleanField(default=True, help_text=b'Display item on my public profile page')),
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
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('suffix', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Ph.D'), (2, b'MD')])),
                ('salutation', models.IntegerField(blank=True, max_length=2, null=True, choices=[(1, b'Mr.'), (2, b'Mrs.'), (3, b'Ms.')])),
                ('middle_name', models.CharField(max_length=50, null=True, blank=True)),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('about', models.TextField(help_text=b'A few sentences about yourself - capsule biography. No HTML allowed.', null=True, blank=True)),
                ('email2', models.EmailField(max_length=75, null=True, verbose_name=b'Secondary Email', blank=True)),
                ('home_phone1', models.CharField(max_length=60, null=True, verbose_name=b'Home Phone', blank=True)),
                ('biz_phone1', models.CharField(max_length=60, null=True, verbose_name=b'Business Phone', blank=True)),
                ('mobile_phone1', models.CharField(max_length=60, null=True, verbose_name=b'Mobile Phone', blank=True)),
                ('fax', models.CharField(max_length=60, null=True, blank=True)),
                ('allow_contact', models.BooleanField(default=True, help_text=b'Allow the public to contact you through CalCentral.')),
                ('show_name', models.BooleanField(default=True, help_text=b'Not currently implemented, for future use.')),
                ('url_personal', models.URLField(null=True, verbose_name=b'Personal website', blank=True)),
                ('url_org', models.URLField(null=True, verbose_name=b'Organization website', blank=True)),
                ('accepted_terms', models.BooleanField(default=False, help_text=b'All users must accept our terms and conditions before doing anything on the site.')),
                ('email_on_follow', models.BooleanField(default=True, help_text=b'Receive email when someone follows you.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('profile', models.OneToOneField(primary_key=True, serialize=False, to='people.Profile')),
                ('office_num', models.CharField(help_text=b'Room number', max_length=30, null=True, blank=True)),
                ('extension', models.CharField(help_text=b'UC Berkeley phone extension, e.g. 3-1234', max_length=30, null=True, blank=True)),
                ('bio_short', models.TextField(help_text=b'Required for all instructors; used on index pages. Limited to around 175 words.')),
                ('bio_long', models.TextField(help_text=b'Used on instructor detail pages.', null=True, blank=True)),
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
                ('profile', models.OneToOneField(primary_key=True, serialize=False, to='people.Profile')),
                ('grad_year', models.IntegerField(max_length=4, null=True, verbose_name=b'Graduation year', choices=[(2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900'), (0, b'0')])),
                ('third_year', models.BooleanField(default=False, verbose_name=b'Is this student on the 3-year plan?')),
                ('j200_inst', models.CharField(help_text=b'e.g. Gorney', max_length=100, null=True, verbose_name=b'J200 Instructor', blank=True)),
                ('funding_amount', models.FloatField(default=0, null=True, blank=True)),
                ('enrollment_date', models.DateField(null=True, blank=True)),
                ('program_length', models.IntegerField(null=True, blank=True)),
                ('equipment_balance', models.FloatField(default=0.0)),
                ('visiting_scholar', models.BooleanField(default=False, help_text=b'Check box if this student is a visiting scholar.')),
                ('employer', models.CharField(max_length=255, null=True, blank=True)),
                ('specialty', models.CharField(help_text=b'e.g. Sports', max_length=128, null=True, blank=True)),
                ('medium', models.IntegerField(blank=True, max_length=4, null=True, choices=[(2, b'Broadcast'), (3, b'Documentary Film'), (4, b'New Media'), (5, b'Newspaper'), (6, b'Magazine'), (8, b'Private Investigating'), (9, b'Public Affairs/Relations'), (10, b'Teaching'), (11, b'Other (Journalism)'), (12, b'Other (Non-Journalism)'), (13, b'Wire Services'), (14, b'Photography'), (15, b'Book Author')])),
                ('prev_emp1', models.CharField(max_length=384, null=True, verbose_name=b'Previous Employer #1', blank=True)),
                ('prev_emp2', models.CharField(max_length=384, null=True, verbose_name=b'Previous Employer #2', blank=True)),
                ('prev_emp3', models.CharField(max_length=384, null=True, verbose_name=b'Previous Employer #3', blank=True)),
                ('notes_exclude', models.BooleanField(default=False, help_text=b'Please do NOT include my notes in the alumni newsletter.', verbose_name=b'Exclude notes')),
                ('notes', models.TextField(help_text=b"Tell us what you're up to, or add general notes on your life, whereabouts and recent projects.", null=True, blank=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('pub_display', models.BooleanField(default=True, help_text=b'If unchecked, record will be hidden even from other J-School alumni, faculty, students and staff.', verbose_name=b'Display Option')),
                ('freelance', models.BooleanField(default=False, verbose_name=b'Freelancing?')),
                ('region', models.IntegerField(blank=True, max_length=4, null=True, choices=[(1, b'New England'), (2, b'East Coast'), (3, b'South'), (4, b'Midwest'), (5, b'Northwest'), (6, b'West Coast'), (7, b'Southwest'), (8, b'New York')])),
                ('prev_intern1', models.CharField(max_length=384, null=True, verbose_name=b'Previous Intership 1', blank=True)),
                ('prev_intern2', models.CharField(max_length=384, null=True, verbose_name=b'Previous Intership 1', blank=True)),
                ('prev_intern3', models.CharField(max_length=384, null=True, verbose_name=b'Previous Intership 1', blank=True)),
                ('first_job', models.CharField(max_length=384, null=True, verbose_name=b'First job out of J-School', blank=True)),
                ('books', models.TextField(null=True, blank=True)),
                ('deceased_notes', models.CharField(max_length=255, null=True, blank=True)),
                ('mia', models.BooleanField(default=False, help_text=b'Unable to contact this person, whereabouts unknown.')),
                ('mia_notes', models.TextField(null=True, blank=True)),
                ('interview', models.BooleanField(default=False, help_text=b'Has this person been interviewed [for xxx?]')),
                ('interview_year', models.IntegerField(default=0, choices=[(2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900'), (0, b'0')])),
                ('interview_notes', models.TextField(null=True, blank=True)),
                ('agents_year', models.IntegerField(default=0, help_text=b'Not sure what this field is for?', null=True, blank=True, choices=[(2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900'), (0, b'0')])),
                ('agents_notes', models.TextField(help_text=b'Not sure what this field is for?', null=True, blank=True)),
                ('event_attend_notes', models.TextField(null=True, blank=True)),
                ('famous_notes', models.TextField(null=True, blank=True)),
                ('volunteer_speak', models.BooleanField(default=False, help_text=b"I'm happy to speak with current students about my career path, what it's like to work at my news outlet (or as a freelancer) and what sort of internship opportunities exist in my workplace.")),
                ('volunteer_committee', models.BooleanField(default=False, help_text=b"I'd like to volunteer to get more involved with planning events and alumni outreach. I might even have suggestions for events in my area.")),
                ('volunteer_interview', models.BooleanField(default=False, help_text=b"I'd like to interview students in my area to help with the admissions process.")),
                ('volunteer_mentor', models.BooleanField(default=False, help_text=b"I'd like to be matched with a student during the school year to provide additional career guidance.")),
                ('volunteer_agent', models.BooleanField(default=False, help_text=b"I'd like to be a Class Agent and serve as a liason between the Alumni Board and my graduating classes.")),
                ('maillist_class', models.BooleanField(default=False, help_text=b'Please add me to my class email list.')),
                ('no_maillists', models.BooleanField(default=False, help_text=b'I do NOT want to receive any email from the journalism school. Please make sure I am NOT on any of the mailing lists.')),
                ('no_reminder', models.BooleanField(default=False, help_text=b'I would like to opt-out from the twice yearly reminder email.')),
                ('suggestions', models.TextField(help_text=b"Do you have suggestions for us about what you'd like to get out of the J-School Alumni Organization? If so, please write us a note and we'll try to incorporate your idea.", null=True, blank=True)),
                ('committee_notes', models.TextField(null=True, blank=True)),
                ('inactive', models.BooleanField(default=False)),
                ('revision', models.IntegerField(help_text=b'This field should increment up when record is updated.', null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.TextField()),
                ('display', models.BooleanField(default=True, help_text=b'Display item on my public profile page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('profile', models.OneToOneField(primary_key=True, serialize=False, to='people.Profile')),
                ('office_num', models.CharField(help_text=b'Room number', max_length=30, null=True, verbose_name=b'Office', blank=True)),
                ('extension', models.CharField(help_text=b'UC Berkeley Phone Extension #-####', max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Staff',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('profile', models.OneToOneField(primary_key=True, serialize=False, to='people.Profile')),
                ('grad_year', models.IntegerField(blank=True, max_length=4, null=True, verbose_name=b'Graduation year', choices=[(2013, b'2013'), (2012, b'2012'), (2011, b'2011'), (2010, b'2010'), (2009, b'2009'), (2008, b'2008'), (2007, b'2007'), (2006, b'2006'), (2005, b'2005'), (2004, b'2004'), (2003, b'2003'), (2002, b'2002'), (2001, b'2001'), (2000, b'2000'), (1999, b'1999'), (1998, b'1998'), (1997, b'1997'), (1996, b'1996'), (1995, b'1995'), (1994, b'1994'), (1993, b'1993'), (1992, b'1992'), (1991, b'1991'), (1990, b'1990'), (1989, b'1989'), (1988, b'1988'), (1987, b'1987'), (1986, b'1986'), (1985, b'1985'), (1984, b'1984'), (1983, b'1983'), (1982, b'1982'), (1981, b'1981'), (1980, b'1980'), (1979, b'1979'), (1978, b'1978'), (1977, b'1977'), (1976, b'1976'), (1975, b'1975'), (1974, b'1974'), (1973, b'1973'), (1972, b'1972'), (1971, b'1971'), (1970, b'1970'), (1969, b'1969'), (1968, b'1968'), (1967, b'1967'), (1966, b'1966'), (1965, b'1965'), (1964, b'1964'), (1963, b'1963'), (1962, b'1962'), (1961, b'1961'), (1960, b'1960'), (1959, b'1959'), (1958, b'1958'), (1957, b'1957'), (1956, b'1956'), (1955, b'1955'), (1954, b'1954'), (1953, b'1953'), (1952, b'1952'), (1951, b'1951'), (1950, b'1950'), (1949, b'1949'), (1948, b'1948'), (1947, b'1947'), (1946, b'1946'), (1945, b'1945'), (1944, b'1944'), (1943, b'1943'), (1942, b'1942'), (1941, b'1941'), (1940, b'1940'), (1939, b'1939'), (1938, b'1938'), (1937, b'1937'), (1936, b'1936'), (1935, b'1935'), (1934, b'1934'), (1933, b'1933'), (1932, b'1932'), (1931, b'1931'), (1930, b'1930'), (1929, b'1929'), (1928, b'1928'), (1927, b'1927'), (1926, b'1926'), (1925, b'1925'), (1924, b'1924'), (1923, b'1923'), (1922, b'1922'), (1921, b'1921'), (1920, b'1920'), (1919, b'1919'), (1918, b'1918'), (1917, b'1917'), (1916, b'1916'), (1915, b'1915'), (1914, b'1914'), (1913, b'1913'), (1912, b'1912'), (1911, b'1911'), (1910, b'1910'), (1909, b'1909'), (1908, b'1908'), (1907, b'1907'), (1906, b'1906'), (1905, b'1905'), (1904, b'1904'), (1903, b'1903'), (1902, b'1902'), (1901, b'1901'), (1900, b'1900'), (0, b'0')])),
                ('funding_amount', models.FloatField(default=0, null=True, blank=True)),
                ('enrollment_date', models.DateField(null=True, blank=True)),
                ('program_length', models.IntegerField(null=True, blank=True)),
                ('visiting_scholar', models.BooleanField(default=False, help_text=b'Check box if this student is a visiting scholar.')),
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
            name='followees',
            field=models.ManyToManyField(help_text=b'People this person is following.', related_name='followers', null=True, to='people.Profile', blank=True),
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
