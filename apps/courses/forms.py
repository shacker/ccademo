from django.db import models
from django.forms import ModelForm, Form
from django import forms
from courses.models import Offering
from django.contrib.auth.models import User


class CourseContactForm(Form):
    '''
    Form to allow students to contact instructors
    '''
    subject = forms.CharField(required=True, max_length=100)
    body = forms.CharField(widget=forms.Textarea,required=True)


class OfferingIntraEditForm(forms.ModelForm):
    '''
    Front-facing form to allow instructors of an offering to edit
    certain details (but not the parent course).
    '''

    class Meta:
    	model = Offering
    	fields = ['title', 'description_override']
	    # title = forms.CharField(required=True, max_length=100)
	    # description_override = forms.CharField(widget=forms.Textarea,required=True)


# For search
class QueryForm(forms.Form):

    q = forms.CharField(label='Title/Keywords', required=False)
