from django.shortcuts import render, get_object_or_404

# from pages.models import Page
from pages.models import Category, Page


def page_detail(request, slug):

	page = get_object_or_404(Page, slug=slug)
	return render(request, 'pages/page_detail.html', locals())


def pages_index(request):

	pages = Page.objects.filter(published=True).exclude(category__slug='news')
	return render(request, 'pages/pages_index.html', locals())


def news_detail(request, slug):

	story = get_object_or_404(Page, slug=slug)
	return render(request, 'pages/news_detail.html', locals())


def news_index(request):

	stories = Page.objects.filter(published=True, category__slug='news').order_by('-timestamp')
	return render(request, 'pages/news_index.html', locals())
