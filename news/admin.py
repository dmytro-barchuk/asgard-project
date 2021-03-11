from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	date_hierarchy = 'created'
	fields = ('news_title', 'image', 'body', 'active')