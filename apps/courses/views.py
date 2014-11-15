from courses.models import Program, Course, Offering, Semester, Assignment, Material, Builder
from people.models import Instructor
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from courses.forms import QueryForm, OfferingIntraEditForm
from postman.models import Message, STATUS_PENDING, STATUS_ACCEPTED
from django.db.models import Q  # For search


def program_home(request):
    """
    Main course listings page
    """

    # First handle course listing selections from programs switcher dropdown
    if request.POST.get('type'):
        return HttpResponseRedirect(reverse('program_sec_courses',
            kwargs={'progslug':request.POST['type'],})) # Redirect after POST

    programs = Program.objects.all()

    return render_to_response(
        'program/index.html',
        locals(),
        context_instance=RequestContext(request)
        )




def programs_list(request):
    """
    Listing of departments
    """

    programs = Program.objects.all()

    return render_to_response(
        'courses/programs_list.html',
        locals(),
        context_instance=RequestContext(request)
        )


def programs_detail(request,slug):
    """
    Single major view
    """

    program = get_object_or_404(Program, slug=slug)

    # Get all instructors in this program. TODO:
    instructors = None



    return render_to_response(
        'courses/programs_detail.html',
        locals(),
        context_instance=RequestContext(request)
        )


def program_sec_courses(request,progslug=False):
    """
    The "Courses" sub-section for a Program of Study, e.g. Business Reporting Courses
    """

    # First handle selections from programs switcher dropdown
    # Redirect after POST
    if request.POST.get('type'):
        program = get_object_or_404(Program, slug=request.POST.get('type'))
        return HttpResponseRedirect(
                    reverse('program_sec_courses',
                            kwargs={'progslug':program.slug,}))

    program = get_object_or_404(Program, slug=progslug)
    programs = Program.objects.all()
    sem = Semester.objects.get(current=True)
    # Get courses that match the current live semester AND are associated with this view's program slug
    offerings = Offering.objects.filter(in_programs__in=(program.id,),semester=sem)

    return render_to_response(
        'program/section-courses.html',
        locals(),
        context_instance=RequestContext(request)
        )


def program_sec_faculty(request,progslug=False):
    """
    The "Faculty" subsection of a Program of Study, e.g. Business Reporting Faculty
    Subdivied into present faculty, lecturers, and previous (inactive) instructors
    """

    program = get_object_or_404(Program, slug=progslug)
    faculty = program.instructors.filter(profile__user__groups__in=(4,),profile__user__is_active=True)
    lecturers = program.instructors.filter(profile__user__groups__in=(5,),profile__user__is_active=True)
    prev_inst = program.instructors.filter(profile__user__is_active=False)

    return render_to_response(
        'program/section-faculty.html',
        locals(),
        context_instance=RequestContext(request)
        )



def offerings_schedule(request, printable=False, sem_id=False):
    """
    Schedule of ALL course offerings - one view handles both calendar and printable view.
    """

    # Construct query params dict for search
    basic_params = {
        'q': request.GET.get('q',''),
        }

    keywords = basic_params['q']
    search_form = QueryForm(basic_params)

    # First handle selections from semester switcher dropdown
    if request.POST.get('sem'):
        sem = get_object_or_404(Semester, pk=request.POST.get('sem'))
        if printable:
            # Redirect to new semester after POST
            return HttpResponseRedirect(
                        reverse(
                            'courses_descriptions_sem',
                            kwargs={'sem_id':sem.pk}))
        else:
            # Redirect to new semester after POST
            return HttpResponseRedirect(
                        reverse(
                            'courses_schedule_sem',
                            kwargs={'sem_id':sem.pk}))

    # Current semester may come through in the URL. If not, default to current semester.
    if sem_id :
        current_sem = get_object_or_404(Semester, pk=sem_id)
    else:
        current_sem = get_object_or_404(Semester, current=True)

    semesters = Semester.objects.filter(live=True).order_by('-id')

    # To generate a unique list of courses (not offerings) for this semester,
    # get all offerings for this semester and derive the distinct internal_titles
    # from their related courses. There's probably a better way to do this query :)
    semofferings = Offering.objects.filter(sec_term=current_sem)
    courselist = semofferings.distinct('course__internal_title').values('course__internal_title')
    courses = Course.objects.filter(internal_title__in=courselist).order_by('internal_title')

    # if keywords exist, filter the results
    if keywords:

        # Use Q object for 'OR' type query
        courses = courses.filter(
                Q(internal_title__icontains=keywords) |
                Q(long_title__icontains=keywords)
            )

    # Which template? Calendar style or printable?
    if printable :
        template = 'courses/descriptions.html'
    else :
        template = 'courses/schedule.html'


    return render_to_response(
        template,
        locals(),
        context_instance=RequestContext(request)
        )



def offering_detail(request, course_sec_id):
    """
    Detail info on a particular course offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)

    # Is this offering already in ScheduleBuilder?
    try:
        builder = Builder.objects.get(profile=request.user.profile, offering=offering)
        scheduled = True
    except:
        pass

    # Allow instructors of a specific offering to override some course details
    if request.user.profile in [i.profile for i in offering.instructors.all()]:
        user_can_edit_offering = True

        if request.method == 'POST':
            course_edit_form = OfferingIntraEditForm(request.POST, instance=offering)
            if course_edit_form.is_valid():
                course_edit_form.save()
                messages.success(request, "Course Offering details overridden")
                return HttpResponseRedirect(reverse('offering_detail',args=[offering.course_sec_id]))

        else:

            '''
            The form's initial values are tricksy because the title and body displayed
            on the *Offering* are inherited from the parent Course object. But when the
            form is saved, it saves overrides into the Offering object itself. To avoid
            presenting a blank form, show inherited values *unless* the object has
            previously been overridden.
            '''

            if not offering.title:
                init_title = offering.course.long_title
            else:
                init_title = offering.title

            if not offering.title:
                init_description_override = offering.course.description
            else:
                init_description_override = offering.description_override

            course_edit_form = OfferingIntraEditForm(
                instance=offering,
                initial={'title': init_title, 'description_override': init_description_override}
                )


    return render_to_response(
        'courses/offering_detail.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_schedule(request, course_sec_id):
    """
    Class schedule for a particular course offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)

    return render_to_response(
        'courses/offering_schedule.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_announcements(request, course_sec_id):
    """
    Announcements displayed to students in a given course offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)
    # announcements = Notification.objects.filter(offering=offering)

    return render_to_response(
        'courses/offering_announcements.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_library(request, course_sec_id):
    """
    Files shared with a course offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)


    return render_to_response(
        'courses/offering_library.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_contact(request, course_sec_id):
    """
    Allows students to make private contact with instructors of a given offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)
    recips = offering.instructors.all()

    return render_to_response(
        'courses/offering_contact.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_policies(request, course_sec_id):
    """
    Simple text field display for grading and policies fields on the Offering model.
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)


    return render_to_response(
        'courses/offering_policies.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_assignments(request, course_sec_id):
    """
    List of assignments given by instructors to students in a given course offering.
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)
    assignments = Assignment.objects.filter(offering=offering)


    return render_to_response(
        'courses/offering_assignments.html',
        locals(),
        context_instance=RequestContext(request)
        )



def offering_assignment_detail(request, assign_id):
    """
    Detail view for individual Assignments (popup only)
    """
    assignment = get_object_or_404(Assignment, id=assign_id)

    return render_to_response(
        'courses/assignment_pop.html',
        locals(),
        context_instance=RequestContext(request)
        )

def offering_materials(request, course_sec_id):
    """
    Materials required by particpants in a given offering
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)
    materials = Material.objects.filter(offering=offering)

    return render_to_response(
        'courses/offering_materials.html',
        locals(),
        context_instance=RequestContext(request)
        )

def offering_material_detail(request, material_id):
    """
    Detail view for class materials requirements (popup only)
    """
    material = get_object_or_404(Material, id=material_id)

    return render_to_response(
        'courses/material_pop.html',
        locals(),
        context_instance=RequestContext(request)
        )


def offering_participants(request, course_sec_id):
    """
    List of students, TAs and instructors associated with a given course offering.
    """

    offering = get_object_or_404(Offering, course_sec_id=course_sec_id)
    students = offering.students.all()
    instructors = offering.instructors.all()

    return render_to_response(
        'courses/offering_participants.html',
        locals(),
        context_instance=RequestContext(request)
        )

def program_detail(request,program_slug):
    """
    Detail info on a particular program
    """

    program = get_object_or_404(Program, slug=program_slug)
    instructors = program.instructors.filter(profile__user__is_active=True)

    # For use in Programs sidebar
    programs = Program.objects.all()

    return render_to_response(
        'courses/program_detail.html',
        locals(),
        context_instance=RequestContext(request)
        )



def course_detail(request, internal_title):
    """
    Detail info on a particular course
    """

    course = get_object_or_404(Course, internal_title=internal_title)
    term = Semester.objects.get(current=True)
    sections = Offering.objects.filter(course=course, sec_term=term).order_by('section')

    # For use in Programs sidebar
    # programs = Program.objects.all()

    return render_to_response(
        'courses/course_detail.html',
        locals(),
        context_instance=RequestContext(request)
        )

