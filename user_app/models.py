""" Models for blog user app """
from django.db import models

# Create your models here.
class BlogUser(models.Model):
    """ Model representing a user in the blog app"""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blog User {self.username}"
     
