from django.forms import ModelForm
from .models import Headmates, Profile

class NewAlterForm(ModelForm):
    class Meta:
        model = Headmates
        fields = ['name', 'pronouns', 'proxy']

class NewSystemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewSystemForm, self).__init__(*args, **kwargs)
        self.fields['system_name'].label = 'What is the name of your system? What do you call yourself and your headmates all together?'

    class Meta:
        model = Profile
        fields = ['system_name']