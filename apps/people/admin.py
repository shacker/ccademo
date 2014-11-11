from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import widgets
from localflavor.us.models import USStateField
from people.constants import STATE_CHOICES_WITH_NULL
from people.models import (
    Alumni, Instructor, Student, Staff,
    Experience, Reference, Award,
    Education, Address, Donation, Profile, Skill,
    UserWidget,
    )

class UserWidgetAdmin(admin.ModelAdmin):
    list_display = ('profile', 'widget', 'order')

class AlumniInline(admin.StackedInline):
     model = Alumni

class InstructorInline(admin.StackedInline):
     model = Instructor

class StudentInline(admin.StackedInline):
     model = Student

class StaffInline(admin.StackedInline):
     model = Staff

class ProfileAdmin(admin.StackedInline):
    model = Profile
    search_fields = ['user__username', 'user__first_name', 'user__last_name',]
    list_display = ('__str__','title','get_primary_email','mobile_phone1')
    raw_id_fields = ('user',)
    inlines = [ StaffInline, StudentInline, AlumniInline, InstructorInline]
    exclude = ('followees',)

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileAdmin, )

class ProfileRelatedAdmin(admin.ModelAdmin):
    search_fields = ['profile__user__username', 'profile__user__first_name', 'profile__user__last_name',]
    raw_id_fields = ('profile',)


class StaffAdmin(ProfileRelatedAdmin):
    list_display = ('__str__','office_num','extension')


class InstructorAdmin(ProfileRelatedAdmin):
    list_display = ('__str__','office_num')

    class Media:
          js = ('/media/js/tiny_mce/tiny_mce.js',
              '/media/js/tiny_mce/admin_textarea.js',)


class StudentAdmin(ProfileRelatedAdmin):
    list_display = ('__str__','enrollment_date',)
    list_filter = ('visiting_scholar', 'enrollment_date',)


class AlumniAdmin(ProfileRelatedAdmin):
    list_display = ('__str__','employer','specialty','medium')
    list_filter = ('medium',)


class DonationAdmin(ProfileRelatedAdmin):
    list_display = ('profile','date','amount')
    raw_id_fields = ('profile',)


class AddressAdminForm(forms.ModelForm):

    # state = USStateField(widget=forms.Select(choices=STATE_CHOICES_WITH_NULL),required=False)

    class Meta:
        model = Address
        fields = '__all__'



class AddressAdmin(ProfileRelatedAdmin):
    list_display = (
        'profile',
        'address_type',
        'street_1',
        'street_2',
        'city',
        'state',
        )
    list_filter = ('address_type',)
    form = AddressAdminForm



class AwardAdmin(ProfileRelatedAdmin):
    list_display = ('profile','title','date_received')


class ExperienceAdminForm(forms.ModelForm):

    # state = USStateField(widget=forms.Select(choices=STATE_CHOICES_WITH_NULL),required=False)

    class Meta:
        model = Experience
        fields = '__all__'




class ExperienceAdmin(ProfileRelatedAdmin):
    list_display = ('profile','title','company','city','state')
    list_filter = ('state','start_date',)
    form = ExperienceAdminForm

class EducationAdmin(ProfileRelatedAdmin):
    list_display = ('profile','diploma','school','start_date','end_date')
    list_filter = ('diploma','start_date',)

class ReferenceAdmin(ProfileRelatedAdmin):
    raw_id_fields = ('profile',)


# Override Django's UserAdmin with our own
# Don't register Profile since it's fields are handled on the User record
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserWidget, UserWidgetAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Alumni, AlumniAdmin)
admin.site.register(Donation,DonationAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Reference,ReferenceAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Skill, ProfileRelatedAdmin)
