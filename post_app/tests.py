""" Modules for blog post app tests """
from django.test import TestCase
from django.core.exceptions import ValidationError
from post_app.models import Posts
from user_app.models import BlogUser


# Create your tests here.
class PostsTests(TestCase):
    ''' Test cases for Posts model '''
   
    def test_valid_post(self):
        ''' Method to test valid post '''
        #pylint: disable=no-member
        author = BlogUser.objects.create(
            username='testuser22',
            email = 'testuser22@example.com',
        )
        post = Posts(
            title="A Valid Title",
            content="This is a valid content with more than ten characters.",
            author_id= author.id
        )
        post.full_clean()  # This will run the validators
        post.save()

def test_invalid_empty_title(self):
    ''' Method to test invalid empty title '''
    post = Posts(
        title="   ",  # Invalid: empty title
        content="This is a valid content with more than ten characters.",
        author_id= 1
    )
    with self.assertRaises(ValidationError):
        post.full_clean()

def test_invalid_short_title(self):
    ''' Method to test invalid short title '''
    post = Posts(
        title="Shrt",  # Invalid: title too short
        content="This is a valid content with more than ten characters.",
        author_id= 1
    )
    with self.assertRaises(ValidationError):
        post.full_clean()

def test_invalid_short_content(self):
    ''' Method to test invalid short content '''
    post = Posts(
        title="A Valid Title",
        content="Too short",  # Invalid: content too short
        author_id= 1
    )
    with self.assertRaises(ValidationError):
        post.full_clean()
