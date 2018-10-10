## Quickstart

Install Django Front End Validators:

```bash
pip install django-front-end-validators
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'front_end_validators',
    ...
)
```

Add URL patterns:

```python
from front_end_validators import urls as front_end_validators_urls


urlpatterns = [
    ...
    url(r'^', include(front_end_validators_urls)),
    ...
]
```

## Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```
