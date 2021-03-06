from courses.models import *
from django.contrib import admin
from django.contrib.admin import widgets

from django import forms

# Custom Admin Action enables making a complete copy of a course (like a Save As...)
def make_copy(modeladmin, request, queryset):
    for obj in queryset:
        # Make a copy in memory
        # Override the ID so the db can auto_increment -- otherwise we overwrite the original!
        # Update the title of the new object
        n = obj
        n.id = None
        n.title = "NEW COPY OF: " + obj.title
        n.save()
        request.user.message_set.create(message="Selected courses have been copied. Remember to set their Instructors and Programs!")
make_copy.short_description = "Make copies of selected courses"



class OfferingAdminForm(forms.ModelForm):
    # To get the list of Instructors in the Course admin form to show only active instructors,
    # need to override the form instance, and in that instance, use our custom active_objects model manager.

    instructors = forms.ModelMultipleChoiceField(
        required=False,
        widget = widgets.FilteredSelectMultiple('Instructors',is_stacked=False),
        queryset = Instructor.objects.all())

    students = forms.ModelMultipleChoiceField(
        required=False,
        widget = widgets.FilteredSelectMultiple('Students',is_stacked=False),
        queryset = Profile.objects.filter(user__is_active=True))



class OfferingAdmin(admin.ModelAdmin):
    list_display = ('__str__','course_sec_id','section','sec_term',)
    search_fields = ('title','course__long_title','course_sec_id')
    actions = [make_copy]
    form = OfferingAdminForm
    raw_id_fields = ('students',)

class CourseAdmin(admin.ModelAdmin):
    search_fields = ('internal_title','long_title',)
    list_display = ('__str__','internal_title','short_title_formatted',)





class MajorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class AssignmentAdmin(admin.ModelAdmin):
    raw_id_fields = ('offering',)

class MaterialAdmin(admin.ModelAdmin):
    raw_id_fields = ('offering',)


class ProgramAdminForm(forms.ModelForm):
    # Custom form for Instructors selection in Program
    instructors = forms.ModelMultipleChoiceField(
                widget = widgets.FilteredSelectMultiple('Instructors',False),
                queryset = Instructor.objects.all(),
                help_text = "")

    description = forms.Textarea()


class ProgramAdmin(admin.ModelAdmin):

    list_display = ('name','prog_majors')
    form = ProgramAdminForm

    def prog_majors(self,obj):
        # Custom method (hack) to display a list of M2M relations in a single Admin colum
        str = ''
        for m in obj.majors.all():
            str += m.name + ", "
        return str


class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'current')


class InstructorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Offering,OfferingAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Semester,SemesterAdmin)
admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Material,MaterialAdmin)
