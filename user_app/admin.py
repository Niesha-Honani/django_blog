""" Models for blog user app """
from django.contrib import admin
from .models import BlogUser

# Register your models here.
admin.site.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('date_joined')

