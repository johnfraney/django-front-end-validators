from django.views.generic import CreateView
from .forms import SampleModelForm
from .models import SampleModel


class SampleModelCreate(CreateView):
    model = SampleModel
    form_class = SampleModelForm
