from django.shortcuts import render, get_object_or_404

from news.models import News


def news_detail(request, slug):

	story = get_object_or_404(News, slug=slug)

	return render(request, 'news/detail.html', locals())

