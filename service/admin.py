from django.contrib import admin
from .models import Category, Service, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	fields = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	# date_hierarchy = '-updated'
	fields = ('category', 'service_name', 'image', 'body', 'active')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	fields = ('name', 'email', 'comment_text')