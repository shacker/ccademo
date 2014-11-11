from django.conf import settings

import json
import requests
import feedparser

from news.models import News
from notifications.models import Notification
from todo.models import Item


def get_intra_news():
    return News.objects.filter(published=True)

def get_chimera_news():
    return feedparser.parse('https://www.cca.edu/news/feed')

def get_nyt_news():
    # NYT API data
    response = requests.get(
        'http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/7.json?api-key={apikey}'.format(apikey=settings.NYT_API_KEY)
        )

    json_data = json.loads(response.text)
    return json_data['results']


def get_library_notifications(request):
    # Library notifications
    return Notification.objects.filter(user=request.user, resolved=False, source__name="Library")

def get_housing_notifications(request):
    # Housing notifications
    return Notification.objects.filter(user=request.user, resolved=False, source__name="Housing")

def get_finaid_notifications(request):
    # Financial aid notifications
    return Notification.objects.filter(user=request.user, resolved=False, source__name="Financial Aid")

def get_helpdesk_tickets(request):
    return Item.objects.filter(assigned_to=request.user, completed=False)
