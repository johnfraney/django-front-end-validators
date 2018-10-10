from django import forms


class FrontEndValidatorsModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        model = self._meta.model
        model_field_map = {}
        for model_field in model._meta.fields:
            model_field_map[model_field.name] = model_field
        for field_name, field in self.fields.items():
            if not hasattr(model, field_name):
                continue
            validators = model_field_map[field_name].validators
            valid_validators = []
            for validator in validators:
                if hasattr(validator, '__name__'):
                    valid_validators.append(f'validators.{validator.__name__}')

            valid_validators_string = str(valid_validators).replace("'", "")

            self.fields[field_name].widget.attrs.update({
                'data-validators': valid_validators_string
            })
