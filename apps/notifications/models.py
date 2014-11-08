from django.db import models
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import truncatewords


NOTIFICATION_TYPE_CHOICES = (
    ('success','Success'),
    ('info','Info'),
    ('warning','Warning'),
    ('danger','Danger'),
)


class Source(models.Model):
    """
    Track sources of campus notification data
    """
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name



class Notification(models.Model):
    """
    Place to put common stuff that extends Profile class.
    """

    user = models.ForeignKey(User)
    source = models.ForeignKey(Source)
    text = models.CharField(max_length=255)
    post_time = models.DateTimeField(default=datetime.datetime.now, help_text='Time posted on remote system')
    act_by = models.DateTimeField(blank=True, null=True, help_text='Action due by date/time')
    resolved = models.BooleanField(default=False)
    resolved_on = models.DateTimeField(blank=True, null=True, help_text='Item marked resolved on date/time')
    level = models.CharField(choices=NOTIFICATION_TYPE_CHOICES, max_length=12, default="info")

    def __unicode__(self):
        return "{user} - {source} - {excerpt}".format(
            user = self.user.username,
            source = self.source.name,
            excerpt = truncatewords(self.text, 10)
            )


