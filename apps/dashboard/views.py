from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from dashboard.widget_functions import *
from dashboard.models import CCAWidget, WIDGETS_DEFAULT_SET
from people.models import UserWidget



def landing(request):
    '''
    Display some info to unauthenticated users
    '''

    if request.user.is_authenticated():
        # Logged in user never needs to see the homepage
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        # Show some generic news and prompt for login

        # Internal news app
        intranews = get_intra_news()

        # CCA main site news (Chimera News)
        ccanews = get_chimera_news()['entries'][0:4]

        nyt_stories = get_nyt_news()[0:4]

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
            profile = request.user.profile
            cca_widget = CCAWidget.objects.get(id=widget_id)
            user_widget = UserWidget(profile=profile, widget=cca_widget, order=0)
            user_widget.save()


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
        UserWidget.objects.get(id=userwidget_id).delete()
        messages.success(request, "Widget removed")

    except:
        messages.error(request, "Error removing widget")

    return HttpResponseRedirect(reverse('dashboard'))


def widget_add(request, widget_id):
    '''
    Takes a CCAWidget ID and combines it with a profile object
    to create a UserWidget instance.
    Redirects immediately without displaying anything.
    '''

    try:
        profile = request.user.profile
        cca_widget = CCAWidget.objects.get(id=widget_id)
        user_widget = UserWidget(profile=profile, widget=cca_widget, order=0)
        user_widget.save()

        messages.success(request, "Widget added")

    except:
        messages.error(request, "Error saving widget")

    return HttpResponseRedirect(reverse('dashboard'))

