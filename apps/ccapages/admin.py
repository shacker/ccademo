from django.contrib import admin
from ccapages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from ccapages.forms import FlatpageForm
from mce_filebrowser.admin import MCEFilebrowserAdmin


class FlatPageAdmin(MCEFilebrowserAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', )
    search_fields = ('url', 'title')

admin.site.register(FlatPage, FlatPageAdmin)
