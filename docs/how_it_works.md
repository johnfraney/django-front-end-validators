Django Front End Validators validates your form inputs as-you-type using the same validation logic specified in your model field's `validators`. It plays nicely with native HTML5 input validation, too.

The heavy lifting of converting model field validators from Python to JavaScript is performed by [Transcrypt](http://www.transcrypt.org/) using the [`transpile_validators` managment command](management_commands.md).

## Example

Let's say you've got this validator on a field called `email`:

```python
from django.core.exceptions import ValidationError


def validate_no_gmail_siblings(value):
    if '+' in value and value.endswith('gmail.com'):
        raise ValidationError(
            "Please use your plain Gmail address"
        )
```

When the field is rendered in a [`FrontEndValidatorsModelForm`](forms.md), it will look like this:

```html
<input type="email" name="email" data-validators="[validators.validate_no_gmail_siblings]">
```

A JavaScript plugin included with the [`{% front_end_validators_js %}` template tag](template_tags.md) checks the input value against the validators listed in `data-validators` in an `oninput` event listener, providing real-time feedback.

If the value fails the `validators.validate_no_gmail_siblings` check, a custom validation error message is added to the field using the [HTML5 Constraint API](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation). This prevents the form from being submitted until the validation error is fixed:

![Email field with failing no Gmail sibling validator](media/validate-no-gmail-siblings.png)
