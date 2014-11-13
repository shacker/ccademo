from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.site.index_template = 'admin/cca_custom_index.html'

urlpatterns = patterns('',

    url(r'^$', 'dashboard.views.landing', name='landing'),
    url(r'^news/(?P<slug>[\w-]+)/$', 'news.views.news_detail',  name='news_detail'),
    url(r'^news/$', 'news.views.news_index',  name='news_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^people/', include('people.urls')),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^scheduler/', include('scheduler.urls')),
	url(r'^todo/', include('todo.urls')),

    # Static/CMS pages
    (r'^tinymce/', include('tinymce.urls')),
    (r'^mce_filebrowser/', include('mce_filebrowser.urls')),

    url(r'^pages/$', 'ccapages.views.index', name='pages_all'),
    url(r'^pages/', include('ccapages.urls')),

    # url(r'^postman/', include('postman.urls')),

	(r'^accounts/login$', 'django_cas_ng.views.login'),
	(r'^accounts/logout$', 'django_cas_ng.views.logout'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

