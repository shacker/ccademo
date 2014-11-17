from django.forms import widgets

from rest_framework import serializers
from courses.models import Course


# Serializers define the API representation.
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='course-detail')
    description = serializers.CharField(max_length=100000)

    class Meta:
        model = Course
        fields = ('id', 'long_title', 'description', 'units')
