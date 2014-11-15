from django import forms
from django.conf import settings
from pages.models import Page
from tinymce.widgets import TinyMCE


class PagesForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 30}))

    class Meta:
        model = Page
        fields = '__all__'
