from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


WIDGET_TYPE_CHOICES = (
    ('list','List'),
    ('html','HTML'),
)

# Note this hierarchy is presented in order of privilege, from most to least
WIDGET_PERMISSION_CHOICES = (
    ('all','Everyone'),
    ('admin','Administrators'),
    ('staff','Staff'),
    ('faculty','Faculty'),
    ('student','Students'),
)

class CCAWidget(models.Model):
    title = models.CharField(max_length=100, default="")
    mandatory = models.BooleanField(default=False, help_text='Show this widget to all users at all times.')
    role_level = models.CharField('Role',choices=WIDGET_PERMISSION_CHOICES, max_length=8, default='all',)
    type = models.CharField('Type',choices=WIDGET_TYPE_CHOICES, max_length=4, default='list',)
    linkurl = models.URLField(blank=True, help_text='Widget title links elsewhwere')
    func = models.CharField('Function to call', max_length=100, null=True, blank=True, help_text='Use for internal data transforms to standard widget list.')
    html = models.TextField('HTML', blank=True, null=True, help_text='Use for abitrary embeddable widgets')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "CCA Widgets"


class UserWidget(models.Model):
    '''
    Through-table used to track the order of widgets used by a user on their Dashboard.
    '''

    profile = models.ForeignKey('people.Profile')
    widget = models.ForeignKey(CCAWidget)
    order = models.IntegerField(default=0)

    def __str__(self):
        return "{username} - {widget}".format(
            username = self.profile.user.username, widget=self.widget
            )


