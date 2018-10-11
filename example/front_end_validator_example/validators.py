from django.core.exceptions import ValidationError
from datetime import datetime


def validate_all_caps(value):
    if value != value.upper():
        raise ValidationError(
            "Value must be all caps"
        )


def validate_four_digits(value):
    if len(str(value)) is not 4:
        raise ValidationError(
            "Value must be four digits"
        )


def validate_future_year(value):
    current_year = datetime.now().year
    if value <= current_year:
        raise ValidationError(
            "{value} is not a future year".format(value=value),
        )


def validate_https(value):
    if not value.startswith('https'):
        raise ValidationError(
            "Value must start with 'https'"
        )


def validate_png(value):
    if not str(value).endswith('.png'):
        raise ValidationError(
            "Image must be a PNG"
        )
