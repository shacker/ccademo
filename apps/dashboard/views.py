from django.shortcuts import render
from news.models import News
from notifications.models import Notification
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import json
import requests
import feedparser


def _get_intra_news():
    return News.objects.filter(published=True)

def _get_chimera_news():
    return feedparser.parse('https://www.cca.edu/news/feed')

def _get_nyt_news():
    # NYT API data
    response = requests.get(
        'http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/7.json?api-key={apikey}'.format(apikey=settings.NYT_API_KEY)
        )

    json_data = json.loads(response.text)
    return json_data['results']



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
        intranews = _get_intra_news()

        # CCA main site news (Chimera News)
        ccanews = _get_chimera_news()['entries'][0:4]

        nyt_stories = _get_nyt_news()[0:4]

        return render(request, 'landing.html', locals())


def dashboard(request):
    """
    Dashboard view
    """

    # Internal news app
    intranews = _get_intra_news()

    # CCA main site news (Chimera News)
    ccanews = _get_chimera_news()['entries'][0:4]

    nyt_stories = _get_nyt_news()[0:4]


    # Library notifications
    lib_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Library")

    # Housing notifications
    housing_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Housing")

    # Financial aid notifications
    finaid_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Financial Aid")






    return render(request, 'dashboard.html', locals())

