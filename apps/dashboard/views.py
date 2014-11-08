from django.shortcuts import render
from news.models import News
from notifications.models import Notification
from django.conf import settings

import json
import requests
import feedparser


def dashboard(request):
    """
    Dashboard view
    """

    intranews = News.objects.filter(published=True)

    # CCA main site news
    feed = feedparser.parse('https://www.cca.edu/news/feed')
    ccanews = feed['entries'][0:4]

    # Library notifications
    lib_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Library")

    # Housing notifications
    housing_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Housing")

    # Financial aid notifications
    finaid_notifs = Notification.objects.filter(user=request.user, resolved=False, source__name="Financial Aid")


    # NYT API data
    response = requests.get(
        'http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/7.json?api-key={apikey}'.format(apikey=settings.NYT_API_KEY)
        )

    json_data = json.loads(response.text)
    nyt_stories = json_data['results'][0:4]
    # End NYT

    return render(request, 'dashboard.html', locals())

