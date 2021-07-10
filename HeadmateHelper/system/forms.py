from django.forms import ModelForm
from .models import Headmates

class NewAlterForm(ModelForm):
    class Meta:
        model = Headmates
        fields = ['name', 'pronouns', 'proxy']