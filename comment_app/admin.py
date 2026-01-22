""" Models for blog comment app """
from django.contrib import admin
from .models import Comments

# Register your models here.
admin.site.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'content', 'created_at')
    search_fields = ('post__title', 'author__username', 'content')
    list_filter = ('created_at',)
