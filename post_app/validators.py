''' validators for post app '''
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import pytz

def validate_empty_title(value):
    ''' Validator to ensure the title is not empty '''
    if not value.strip():
        raise ValidationError(
            _('$(value) cannot be empty or whitespace only.'),
            params={'value': value},
        )

def validate_title_length(value):
    ''' Validate title is at least 5 characters long'''
    if len(value) < 5:
        raise ValidationError(
            _('Title must be at least 5 characters long.'),
            params={'value': value},
        )

def validate_content_length(value):
    ''' Validator to ensure content length is at least 10 characters '''
    if len(value) < 10:
        raise ValidationError(
            _('Content must be at least 10 characters long.'),
            params={'value': value},
        )

def validate_not_utc_time(value):
    ''' Validator to ensure datetime is no UTC time'''
    # validate timezone aware, not UTC and project is using local timezone
    if timezone.is_naive(value):
        raise ValidationError(
            _('Date time must be timezone aware.'),
            params={'value': value},
        )

    if value.tzinfo == pytz.utc:
        raise ValidationError(
            _('Date time should not be in UTC timezone.'),
            params={'value': value},
        )
