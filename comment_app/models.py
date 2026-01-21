from django.db import models

# Create your models here.
class Comments(models.Model):
    """ Model representing a comment on a blog post """
    # One Post --> Many Comments
    post = models.ForeignKey('post_app.Posts', on_delete=models.CASCADE, related_name='comments')
    # Many Comments --> One Blog User
    author = models.ForeignKey('user_app.BlogUser', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=255,null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
