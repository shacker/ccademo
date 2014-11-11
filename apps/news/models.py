from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

import datetime


class News(models.Model):
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(default="")
    author = models.ForeignKey(User)
    body = models.TextField(help_text='Story text')
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('news_detail',
            kwargs={'slug': self.slug,})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"