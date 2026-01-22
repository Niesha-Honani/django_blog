""" admin configuration for blog post app """
from django.contrib import admin
from .models import Posts

# Register your models here.
admin.site.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username', 'content')
    list_filter = ('created_at',)