from django.contrib import admin
from dashboard.models import CCAWidget

class CCAWidgetAdmin(admin.ModelAdmin):
	list_display = ('title', 'role_level', 'mandatory', 'func')

admin.site.register(CCAWidget, CCAWidgetAdmin)