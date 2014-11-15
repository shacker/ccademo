import json
import requests
import feedparser
from django.conf import settings
from pages.models import Page
from notifications.models import Notification
from todo.models import Item


class WidgetFunctions():

    def get_ets_news(widget_instance, user):
        return {
            'object_list': Page.objects.filter(published=True, category__slug='news').order_by('-timestamp')
            }

    def get_chimera_news(widget_instance, user):
        data = feedparser.parse('https://www.cca.edu/news/feed')['entries'][0:4]

        # Rewrite data to conform internal links
        for d in data:
            d['get_absolute_url'] = d['link']

        return {
            'object_list': data
            }

    def get_nyt_news(widget_instance, user):
        # NYT API data
        response = requests.get(
            'http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/7.json?api-key={apikey}'.format(apikey=settings.NYT_API_KEY)
            )

        json_data = json.loads(response.text)
        data = json_data['results'][0:4]

        # Rewrite data to conform internal links
        for d in data:
            d['get_absolute_url'] = d['url']

        return {
            'object_list': data
            }


    def get_library_notifications(widget_instance, user):
        return {
            'object_list': Notification.objects.filter(user=user, resolved=False, source__name="Library")
        }

    def get_housing_notifications(widget_instance, user):
        # Housing notifications
        return {
            'object_list': Notification.objects.filter(user=user, resolved=False, source__name="Housing")
        }

    def get_finaid_notifications(widget_instance, user):
        # Financial aid notifications
        return {
            'object_list': Notification.objects.filter(user=user, resolved=False, source__name="Financial Aid")
        }

    def get_helpdesk_tickets(widget_instance, user):
        return {
            'object_list': Item.objects.filter(assigned_to=user, completed=False)[0:4]
        }
