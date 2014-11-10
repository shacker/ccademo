from django.conf.urls import patterns

urlpatterns = patterns('ccapages.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)
