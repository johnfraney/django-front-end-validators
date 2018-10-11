# Forms


## `FrontEndValidatorsModelForm`

This class extends Django's `ModelForm` to add a `data-validators` attribute to any field that contains validators. `data-validators` lists references to JavaScript validator functions.

For example, if we have a field called `https_url` with a validator function `validate_https()`, the form input for that field will look like this:

```html
<input type="url" name="https_url" data-validators="[validators.validate_https]">
```

A JavaScript plugin included in the [`{% front_end_validators_js %}` template tag](template_tags.md) checks the input value against the validators in an `oninput` event listener.
