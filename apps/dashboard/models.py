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
