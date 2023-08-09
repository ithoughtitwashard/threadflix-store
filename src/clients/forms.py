from django.contrib.auth.forms import AuthenticationForm
from django import forms

from clients.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'placeholder': 'example09'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4',
        'placeholder': ''
    }))
    class Meta:
        model = User
        field = ('username', 'password')
