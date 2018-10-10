from front_end_validators.forms import FrontEndValidatorsModelForm
from .models import SampleModel


class SampleModelForm(FrontEndValidatorsModelForm):
    class Meta:
        model = SampleModel
        fields = '__all__'
