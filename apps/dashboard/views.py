from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from dashboard.widget_functions import *


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

    # Internal news app
    intranews = get_intra_news()

    # CCA main site news (Chimera News)
    ccanews = get_chimera_news()['entries'][0:4]

    # NYT
    nyt_stories = get_nyt_news()[0:4]

    # Financial aid
    finaid_notifs = get_finaid_notifications(request)

    # Housing
    housing_notifs = get_housing_notifications(request)

    # Library
    lib_notifs = get_library_notifications(request)

    # Tickets
    tickets = get_helpdesk_tickets(request)

    return render(request, 'dashboard.html', locals())

