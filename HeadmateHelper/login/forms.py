from django.forms import ModelForm
from system.models import Profile, Headmates

class NewSystemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewSystemForm, self).__init__(*args, **kwargs)
        self.fields['system_name'].label = 'What is the name of your system? What do you call yourself and your headmates all together?'

    class Meta:
        model = Profile
        fields = ['system_name']