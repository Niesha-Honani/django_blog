""" Models for blog user app """
from django.db import models
from user_app.validators import validate_username, validate_email_domain, validate_date_joined

# Create your models here.
class BlogUser(models.Model):
    """ Model representing a user in the blog app"""
    username = models.CharField(max_length=150, unique=True, validators=[validate_username])

    email = models.EmailField(unique=True, validators=[validate_email_domain])
    date_joined = models.DateTimeField(auto_now_add=True, validators=[validate_date_joined])

    def __str__(self):
        return f"Blog User: {self.username} - {self.email} - Joined on {self.date_joined}"
