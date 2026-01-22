""" Models for blog post app """
from django.db import models
from .validators import(
    validate_empty_title,
    validate_title_length,
    validate_content_length,
    validate_not_utc_time,
)
# Create your models here
class Posts(models.Model):
    """ Model representing a blog post """
    title = models.CharField(
        max_length=200, null=False,
        validators=[validate_empty_title, validate_title_length])

    content = models.TextField(
        max_length=1000, null=False,
        validators=[validate_content_length])

    author = models.ForeignKey('user_app.BlogUser', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(
        auto_now_add=True,
        validators=[validate_not_utc_time])

    def __str__(self):
        return f"Post: {self.title} by {self.author}"
