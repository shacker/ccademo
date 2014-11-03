from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^$', 'dashboard.views.dashboard', name='dashboard'),
    url(r'^news/(?P<slug>[\w-]+)/$', 'news.views.news_detail',  name='news_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/', include('people.urls')),

)
