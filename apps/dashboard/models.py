from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# IDs of widgets that must appear for everyone
# Initially, just preventing deletion of these.
# TODO: Instantiate new users with this set
WIDGETS_DEFAULT_SET = [1, 2, 3,]

WIDGET_TYPE_CHOICES = (
    ('list','List'),
    ('html','HTML'),
)

class CCAWidget(models.Model):
    title = models.CharField(max_length=100, default="")
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

    def user_can_delete_widget(self):
        # Don't allow deletion of default widget set
        if self.widget.id not in WIDGETS_DEFAULT_SET:
            return True


