from rest_framework import viewsets
from courses.models import Course, Offering
from api.serializers import CourseSerializer, OfferingSerializer, ProfileSerializer
from people.models import Profile

# ViewSets define the view behavior.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class OfferingViewSet(viewsets.ModelViewSet):
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
