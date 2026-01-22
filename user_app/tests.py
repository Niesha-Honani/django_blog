""" Modules for blog user app tests """
from django.test import TestCase
from django.core.exceptions import ValidationError
from user_app.models import BlogUser

class BlogUserTests(TestCase):
    """ Test cases for BlogUser model """

    def test_valid_user(self):
        ''' Method to test valid user '''
        user = BlogUser(
            username="test_user2",
            email="test_user2@example.com"
        )
        user.full_clean()  # This will run the validators
        user.save()

    def test_invalid_username(self):
        ''' Method to test invalid username '''
        user = BlogUser(
            username="ab", # Invalid: too short
            email="ab@phantom.com"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()


    def test_invalid_email_domain(self):
        ''' Method to test invalid email domain '''
        user = BlogUser(
            username="bad_email_user",
            email="bad_email_user@ggxa.ss"
        )
        with self.assertRaises(ValidationError):
            user.full_clean()
