from django.db import models
from courses import constants
from people.models import Profile, Instructor, Student
from django.contrib.auth.models import User
import datetime

'''
A program ("Ceramics") can be in many majors.
A course offering can be in many programs.
'''


class Room(models.Model):
    """
    A resource subclass to define rooms.
    """
    name = models.CharField("Room Name",max_length=64,blank=True, default='')
    number = models.CharField("Room Number",max_length=64,blank=True, default='')
    has_screen = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s %s" % (self.name, self.number)



class Program(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=False)
    instructors = models.ManyToManyField(Instructor) # All instructors who have ever taught in this program

    def __unicode__(self):
      return self.name



class Semester(models.Model):
    name = models.CharField(max_length=96)
    current = models.NullBooleanField(unique=True,null=True,help_text="Select &quot;Yes&quot; for the current semester, &quot;Unknown&quot; for all others. Ignore the &quot;No&quot; option. Only one semester may be marked current at a time.")
    ord_by = models.IntegerField(null=True, blank=True)
    live = models.BooleanField(default=False, help_text='When checked, this semester&apos;s schedule will appear on the public site.')

    def __unicode__(self):
        return self.name




class Course(models.Model):
    long_title = models.CharField(max_length=100)
    internal_title = models.CharField(max_length=16)
    short_title_formatted = models.CharField(max_length=64)
    units = models.IntegerField(choices=constants.UNIT_TYPE_CHOICES, blank=True, null=True)
    course_type = models.IntegerField(choices=constants.COURSE_TYPE_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    restrictions = models.TextField(null=True,blank=True)
    programs = models.ManyToManyField(Program,blank=True, null=True)

    def __unicode__(self):
      return self.long_title


class Offering(models.Model):
    '''A particular instance of a Course, held in a given semester'''

    course = models.ForeignKey(Course)
    course_sec_id = models.IntegerField('Section ID (from datatel)', unique=True)
    section = models.CharField('Section',choices=constants.LARGE_NUMBER_RANGE, max_length=4, blank=True, null=True)
    title = models.CharField(blank=True,null=True,max_length=384,help_text='If present, overrides same field in Course model.')
    sec_term = models.ForeignKey(Semester)
    instructors = models.ManyToManyField(Instructor, null=True, blank=True)
    students = models.ManyToManyField(Profile, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    end_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    location = models.ForeignKey(Room,help_text='If location is mixed, such as &quot;Monday in the Mission, Thursday RM 104&quot; then select Other as location and fill in Other Location field.')
    location_other = models.CharField(blank=True, max_length=100)
    grading = models.TextField(blank=True,null=True)
    policies = models.TextField(blank=True,null=True)
    fee = models.BooleanField(default=False,help_text='Fee required to take this course?')
    enroll_lim = models.IntegerField('Enrollment limit',choices=constants.LARGE_NUMBER_RANGE,help_text='Enrollment limit for this course (select nothing if there isn&apos;t one.)',blank=True,null=True)
    description_override = models.TextField(blank=True,null=True,help_text='If present, overrides same field in Course model.')
    restrictions_override = models.TextField(null=True,blank=True,help_text='If present, overrides same field in Course model.')
    # eval_group = models.ForeignKey(EvalQGroup,verbose_name='Course evaluation question set',null=True,blank=True,related_name="course_eval_group",
    #     help_text="Which COURSE evaluations question set should this course be evaluated with at the end of the semester?")
    # instr_eval_group = models.ForeignKey(EvalQGroup,verbose_name='Instructor evaluation question set',null=True,blank=True,related_name="instr_eval_group",default=2,
    #     help_text="Which INSTRUCTOR evaluations question set should this course be evaluated with at the end of the semester?")
    # programs = models.ManyToManyField(Program,blank=True)

    def __unicode__(self):
      return self.title if self.title else self.course.long_title

    def description(self):
        return self.description_override if self.description_override else self.course.description

    def restrictions(self):
        return self.restrictions_override if self.restrictions_override else self.course.restrictions

    def get_members(self):
        '''
        Obtain all members of this course offering, which includes its instructors and TAs.
        '''

        all_members = set()

        # Designated admins
        for u in self.students.all():
          all_members.add(u.id)

        # Assigned instructors
        for i in self.instructors.all():
          all_members.add(i.profile.user.id)

        # additional queries here

        return User.objects.filter(pk__in=all_members)


class Assignment(models.Model):
    '''Assignments given to students in a given course offering'''

    offering = models.ForeignKey(Offering)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __unicode__(self):
      return self.title


class Material(models.Model):
    '''Materials students will need during a given course offering'''

    offering = models.ForeignKey(Offering)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    obtain_at = models.CharField(blank=True, max_length=100)
    url = models.URLField(blank=True,null=True)
    cost = models.DecimalField('Approximate Cost',blank=True,null=True,max_digits=8,decimal_places=2)

    def __unicode__(self):
      return self.title



# ====================
# This model holds raw datatel data and is only to be used by importer scripts

class ImporterCourses(models.Model):
    action = models.CharField(max_length=2, blank=True)
    course_sec_id = models.CharField(max_length=128, blank=True)
    course = models.CharField(max_length=128, blank=True)
    section = models.CharField(max_length=128, blank=True)
    sec_short_title = models.CharField(max_length=128, blank=True)
    sec_desc = models.TextField(blank=True)
    sec_start_date = models.CharField(max_length=128, blank=True)
    sec_end_date = models.CharField(max_length=128, blank=True)
    dept = models.CharField(max_length=128, blank=True)
    sec_csxl = models.CharField(max_length=128, blank=True)
    sec_term = models.CharField(max_length=128, blank=True)
    short_title_formatted = models.CharField(max_length=128, blank=True)

    class Meta:
        managed = False
        db_table = 'importer_courses'