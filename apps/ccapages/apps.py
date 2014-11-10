from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class FlatPagesConfig(AppConfig):
    name = 'ccapages'
    verbose_name = _("CCA Flat Pages")
