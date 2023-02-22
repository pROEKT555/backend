from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import Register

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['login', 'passworld', 'email']
        
        widgets = {
            'login': TextInput(attrs={'placeholder': 'Логін'}),
            'passworld': PasswordInput(attrs={'placeholder': 'Пароль'}),
            'email': EmailInput(attrs={'placeholder': 'Email'})
        }
