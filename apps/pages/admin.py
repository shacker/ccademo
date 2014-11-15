from django.contrib import admin
from pages.models import Category, Page
from pages.forms import PagesForm
from mce_filebrowser.admin import MCEFilebrowserAdmin


class PageAdmin(MCEFilebrowserAdmin):
	form = PagesForm
	list_display = ('title', 'author', 'published', 'timestamp')
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category)
