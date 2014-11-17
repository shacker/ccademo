from rest_framework import viewsets
from courses.models import Course
from api.serializers import CourseSerializer


# ViewSets define the view behavior.
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
