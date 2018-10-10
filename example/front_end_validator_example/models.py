from django.db import models
from . import validators


class SampleModel(models.Model):
    future_year = models.PositiveIntegerField(
        validators=[
            validators.validate_four_digits,
            validators.validate_future_year,
        ],
        help_text="A four-digit year in the future"
    )
    all_caps = models.CharField(
        max_length=100,
        validators=[
            validators.validate_all_caps,
        ],
        help_text="A value in ALL CAPS"
    )
    https_url = models.URLField(
        'HTTPS URL',
        max_length=200,
        validators=[
            validators.validate_https,
        ],
        help_text="A URL starting with 'https'. Works on top of native HTML5 URL validation."
    )
    png_image = models.ImageField(
        'PNG image',
        validators=[
            validators.validate_png,
        ],
        help_text="An image file with a .png extension"
    )
