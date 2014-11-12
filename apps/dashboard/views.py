from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from dashboard.widget_functions import *
from dashboard.models import CCAWidget, WIDGETS_DEFAULT_SET
from people.models import UserWidget

def create_user_widget(request, widget_id):
    # Given a CCAWidget ID, creates UserWidget for requesting user
    try:
        profile = request.user.profile
        cca_widget = CCAWidget.objects.get(id=widget_id)
        user_widget = UserWidget(profile=profile, widget=cca_widget, order=0)
        user_widget.save()
        return True

    except:
        return False


def landing(request):
    '''
    Display some info to unauthenticated users
    '''

    if request.user.is_authenticated():
        # Logged in user never needs to see the homepage
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        # Show some generic news and prompt for login

        return render(request, 'landing.html', locals())


def dashboard(request):
    """
    Dashboard view.
    Template tag in dashboard.html handles widget logic.
    """

    # This user's used widgets
    userwidgets = UserWidget.objects.filter(profile=request.user.profile).order_by('order')

    # If user has no widgets, instantiate the default set
    if userwidgets.count() == 0:
        for widget_id in WIDGETS_DEFAULT_SET:
            create_user_widget(request, widget_id)


    # Get a list of ids of parent widget objects in use by this user
    usedwidgets = [u.widget.id for u in userwidgets]

    # The set of all parent widgets minus the set of widgets the user already has installed
    otherwidgets = CCAWidget.objects.exclude(id__in=usedwidgets)

    return render(request, 'dashboard/dashboard.html', locals())



def widget_remove(request, userwidget_id):
    '''
    Remove a UserWidget instance from User's profile.
    Redirects immediately without displaying anything.
    '''

    try:
        user_widget = UserWidget.objects.get(id=userwidget_id)
    except:
        messages.error(request, "That widget does not exist.")

    if user_widget.user_can_delete_widget():
        try:
            user_widget.delete()
            messages.success(request, "Widget removed")

        except:
            messages.error(request, "Error removing widget")

    else:
            messages.error(request, "Sorry, this widget is required.")

    return HttpResponseRedirect(reverse('dashboard'))


def widget_add(request, widget_id):
    '''
    Takes a CCAWidget ID and combines it with a profile object
    to create a UserWidget instance.
    Redirects immediately without displaying anything.
    '''

    try:
        create_user_widget(request, widget_id)
        messages.success(request, "Widget added")

    except:
        messages.error(request, "Error saving widget")

    return HttpResponseRedirect(reverse('dashboard'))


@csrf_exempt
def widgets_reorder(request):
    '''
    Takes an ajax posted list of ordered IDs of userwidgets
    and saves new ordering data to the db.
    '''
    user_widget_ids = request.POST.getlist('datasorted[]')

    # Items arrive in order, so all we need to do is increment up from one, saving
    # "counter" as the new priority for the current object.
    # Python "enumerate()" is built-in counter
    for counter, w_id in enumerate(user_widget_ids):
        update_widget = UserWidget.objects.get(id=w_id)
        update_widget.order = counter
        update_widget.save()

    # All views must return an httpresponse of some kind ... without this we get
    # error 500s in the log even though things look peachy in the browser.
    # Return Apache 202 ("Accepted")
    return HttpResponse(status=202)


