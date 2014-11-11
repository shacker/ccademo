from django.contrib import admin
from dashboard.models import CCAWidget

class CCAWidgetAdmin(admin.ModelAdmin):
	list_display = ('title', 'func')

admin.site.register(CCAWidget, CCAWidgetAdmin)