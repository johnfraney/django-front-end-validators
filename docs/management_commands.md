## `transpile_validators`

This management command uses [Transcrypt](http://www.transcrypt.org/) to convert your project's `validators.py` file from Python to JavaScript.

The transpiled JavaScript is placed in alongside your `validators.py` file in the following directory:

| Transcrypt Version | Output Directory |
| ------------------ | ---------------- |
| 3.6                | `__javascript__` |
| 3.7                | `__target__`     |

!!! info
    The relevant directory should be added to your project's `STATICFILES_DIRS` settings.
