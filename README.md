# Django Front End Validators

[
![PyPI](https://img.shields.io/pypi/v/django-front-end-validators.svg)
![PyPI](https://img.shields.io/pypi/pyversions/django-front-end-validators.svg)
![PyPI](https://img.shields.io/pypi/djversions/django-front-end-validators.svg)
![PyPI](https://img.shields.io/pypi/l/django-front-end-validators.svg)
](https://pypi.org/project/django-front-end-validators/)
[![TravisCI](https://travis-ci.org/johnfraney/django-front-end-validators.svg?branch=master)](https://travis-ci.org/johnfraney/django-front-end-validators)

Use model field validator functions for front end JS validation


## Documentation

Documentation is available in the [docs directory](./docs/index.md) and at https://johnfraney.github.io/django-front-end-validators.


## Restrictions

This package uses Transcrypt 3.7 to transpile Python validator functions into a newer version of JavaScript (ES6/ES2015) that not all browsers understand.

See here for browser compatibility: https://caniuse.com/#feat=es6-module


## Credits

Tools used in rendering this package:

[Transcrypt](http://www.transcrypt.org/)

[Cookiecutter](https://github.com/audreyr/cookiecutter)

[`cookiecutter-djangopackage`](https://github.com/pydanny/cookiecutter-djangopackage)



## Code of Conduct

Everyone interacting in the project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).
