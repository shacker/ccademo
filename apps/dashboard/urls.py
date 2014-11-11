from django.conf.urls import patterns, include, url
from dashboard import views

# URLs dealing with profiles

urlpatterns = patterns('',
    url(r'^$',
        views.dashboard,
        name='dashboard'),

    url(r'^widget/(?P<userwidget_id>\d{1,9})/remove$',
        views.widget_remove,
        name='widget_remove'),

    url(r'^widget/(?P<widget_id>\d{1,9})/add$',
        views.widget_add,
        name='widget_add'),

)

