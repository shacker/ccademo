from django.conf.urls import patterns, include, url
from rest_framework import routers, viewsets
from api.viewsets import CourseViewSet, OfferingViewSet, ProfileViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'offerings', OfferingViewSet)

urlpatterns = patterns('',

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)