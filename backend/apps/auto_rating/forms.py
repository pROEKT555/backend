from django.forms import ModelForm, TextInput
from content.models import Check

class CheckForm(ModelForm):
    class Meta:
        model = Check
        fields = ['test', 'name', 'rating']

        widgets = {
            'test': TextInput(),
            'name': TextInput(),
            'rating': TextInput()
        }
