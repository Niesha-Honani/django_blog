""" Module containing custom validators for user app """
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

#Custom Validators - Validators are business rules to validate data before saving to the database.
# Busines Rules live with the data model, not with tests or views.

def validate_username(value):
    """
    Validate that the username contains only alphanumeric characters and underscores,
    and is between 3 and 30 characters long.
    """
    if not re.match(r'^[a-zA-Z0-9_]{3,30}$', value):
        raise ValidationError(
            _('Username must be 3-30 characters long and can only contain letters, numbers, and underscores.'),
            params={'value': value},
        )

def validate_email_domain(value):
    """
    Validate that the email belongs to a specific domain (e.g., example.com).
    """
    domain = value.split('@')[-1]
    if domain.lower() not in ['example.com', 'example.org']:
        raise ValidationError(
            _('Email must be from the domain example.com or example.org.'),
            params={'value': value},
        )
def validate_date_joined(value):
    """
    Validate that the date_joined is not in the future.
    """
    if value > timezone.now():
        raise ValidationError(
            _('Date joined cannot be in the future.'),
            params={'value': value},
        )
