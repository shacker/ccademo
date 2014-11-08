from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^$', 'dashboard.views.landing', name='landing'),
    url(r'^dashboard/$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^news/(?P<slug>[\w-]+)/$', 'news.views.news_detail',  name='news_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/', include('people.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^scheduler/', include('scheduler.urls')),
	url(r'^todo/', include('todo.urls')),


    # url(r'^postman/', include('postman.urls')),

	(r'^accounts/login$', 'django_cas_ng.views.login'),
	(r'^accounts/logout$', 'django_cas_ng.views.logout'),

)
