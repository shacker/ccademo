from django.shortcuts import render
from news.models import News
from django.conf import settings

import json
import requests


def dashboard(request):
    """
    Homepage view
    """

    news = News.objects.filter(published=True)

    # NYT API data
    response = requests.get(
        'http://api.nytimes.com/svc/mostpopular/v2/mostshared/all-sections/7.json?api-key={apikey}'.format(apikey=settings.NYT_API_KEY)
        )

    json_data = json.loads(response.text)
    nyt_stories = json_data['results'][0:4]
    # End NYT

    return render(request, 'dashboard.html', locals())

