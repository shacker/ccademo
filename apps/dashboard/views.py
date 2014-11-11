from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from dashboard.widget_functions import *
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
    Dashboard view
    """

    widgets = UserWidget.objects.filter(profile=request.user.profile).order_by('order')

    # For each user-selected widget, run the associated function to get data

    return render(request, 'dashboard/dashboard.html', locals())

