from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CCAWidget(models.Model):
    title = models.CharField(max_length=100, default="")
    linkurl = models.URLField(blank=True, help_text='Widget title links elsewhwere')
    func = models.CharField('Function to call', max_length=100)

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
        return "{username} - {widget}".format(username = self.profile.user.username, widget=self.widget)
