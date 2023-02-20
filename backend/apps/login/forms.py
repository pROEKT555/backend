from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['login', 'passworld', 'email']
        
        widgets = {
            'login': TextInput(attrs={'placeholder': 'Логін'}),
            'passworld': PasswordInput(attrs={'placeholder': 'Пароль'}),
            'email': EmailInput(attrs={'placeholder': 'Email'})
        }
