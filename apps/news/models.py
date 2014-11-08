from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime


class News(models.Model):
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=100, default="")
    slug = models.SlugField(default="")
    author = models.ForeignKey(User)
    body = models.TextField(help_text='Story text')
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"