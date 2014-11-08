from django.contrib import admin
from notifications.models import Source, Notification

class NotificationAdmin(admin.ModelAdmin):
	list_display = ('user', 'source', 'post_time', 'resolved', 'level', 'text')
	# prepopulated_fields = {"slug": ("title",)}
	raw_id_fields = ('user',)


admin.site.register(Source)
admin.site.register(Notification, NotificationAdmin)