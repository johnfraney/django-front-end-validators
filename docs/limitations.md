## Only function-style validators

Although Django supports both [class-based and function validators](https://docs.djangoproject.com/en/dev/ref/validators/), this package supports only validators written as functions. If supporting class-based validators is important to you, please open an [issue](https://github.com/johnfraney/django-front-end-validators/issues).


## No i18n

Because the transpiled JavaScript runs in the browser, it doesn't have direct access to the database or filesystem. If you know of a way to get this to work, please open a [pull request](https://github.com/johnfraney/django-front-end-validators/pulls)!


## Example

The [Django validators documentation](https://docs.djangoproject.com/en/dev/ref/validators/#writing-validators) gives this as en example `ValidationError`:

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
```

After removing `ugettext_lazy`, we get a validator that will work on the front end:

```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )
```
