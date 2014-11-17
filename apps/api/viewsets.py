from rest_framework import viewsets
from courses.models import Course, Offering
from api.serializers import CourseSerializer, OfferingSerializer


# ViewSets define the view behavior.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# ViewSets define the view behavior.
class OfferingViewSet(viewsets.ModelViewSet):
    queryset = Offering.objects.all()
    serializer_class = OfferingSerializer
