from django.forms import widgets
from django.core.urlresolvers import reverse

from rest_framework import serializers
from courses.models import Course, Offering
from people.models import Instructor

# Serializers define the API representation.


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='course-detail')
    description = serializers.CharField(max_length=100000)

    class Meta:
        model = Course
        fields = ('id', 'long_title', 'description', 'units')


class OfferingSerializer(serializers.ModelSerializer):
    '''
    Serialized representation of a course offering, with calculated fields
    '''

    parent_course_title = serializers.SerializerMethodField('get_parent_title')
    calculated_title = serializers.SerializerMethodField('get_calculated_title')
    parent_course_id = serializers.SerializerMethodField('get_parent_course')
    offering_link = serializers.HyperlinkedIdentityField(view_name='offering-detail')
    instructors = serializers.SerializerMethodField('instructors_list_to_dicts')


    class Meta:
        model = Offering
        # Uncomment if we want to specify fields
        # fields = ('course_sec_id', 'calculated_title',)
        lookup_field = 'course_sec_id'  # Use this for Offering URLs, not the pk ID


    def get_calculated_title(self, obj):
        # Return Offering title if it exists, else the parent course title
        if obj.title:
            return obj.title
        else:
            return obj.course.long_title

    def get_parent_title(self, obj):
        # Return parent course title only
        return obj.course.long_title

    def get_parent_course(self, obj):
        return obj.course.id

    def instructors_list_to_dicts(self, obj):
        # Instructors as a list of dictionaries; one dict for each author in the byline
        return [{
            "name": i.profile.get_display_name,
            "profile_url": reverse('people_profile_detail', args=[i.profile.user.username])}
            for i in obj.instructors.all()
            ]
