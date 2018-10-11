## About

Django Front End Validators allows you to reuse server-side [model field validators](https://docs.djangoproject.com/en/dev/ref/validators/) to perform front end form validation in JavaScript.

## Quickstart

#### Install Django Front End Validators

```bash
pip install django-front-end-validators
```

#### Update `INSTALLED_APPS`

```python
INSTALLED_APPS = (
    ...
    'front_end_validators',
    ...
)
```

#### Configure settings

```python
# The directory into which Transcrypt transpiles JS
STATICFILES_DIRS = [
    # Transcrypt 3.7:
    'your_project/__target__'
    # Transcrypt 3.6:
    'your_project/__javascript__',
]

# The path to your validators.py file
VALIDATORS_FILE = os.path.join(BASE_DIR, 'your_project/validators.py')
```

#### Add template tag

```html+django
{% load front_end_validators %}<!doctype html>
<html>
  <head>
    {{ form.media.css }}
  </head>
<body>
  {% block content %}{% endblock %}
  {% front_end_validators_js %}
  {{ form.media.js }}
</body>
</html>
```

#### Transpile validators

```bash
./manage.py transpile_validators
```

#### Write forms

```python
from front_end_validators.forms import FrontEndValidatorsModelForm
from .models import YourModel


class YourModelForm(FrontEndValidatorsModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'
```

## Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```
