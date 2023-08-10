from django import forms
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def user_authentication_authorization(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request, user)
        return HttpResponseRedirect(redirect_to=reverse('index'))


def login_form_fields():
    username = _create_input('example09', 'TextInput')
    password = _create_input('', 'PasswordInput')
    return username, password


def register_form_fields():
    first_name = _create_input('Thread', 'TextInput')
    last_name = _create_input('Flix', 'TextInput')
    username = _create_input('example09', 'TextInput')
    email = _create_input('example@mail.com', 'EmailInput')
    password1 = _create_input('', 'PasswordInput')
    password2 = _create_input('', 'PasswordInput')
    return first_name, last_name, username, email, password1, password2


def profile_form_fields_without_image():
    first_name = _create_input('', 'TextInput')
    last_name = _create_input('', 'TextInput')
    username = _create_input('', 'TextInput', readonly=True)
    email = _create_input('', 'EmailInput', readonly=True)
    return first_name, last_name, username, email


def _create_input(placeholder: str, input_type: str, readonly: bool = False):
    attrs = {
        'class': 'form-control py-4',
        'placeholder': placeholder,
        'readonly': readonly
    }
    if input_type == 'TextInput':
        return forms.CharField(widget=forms.TextInput(attrs=attrs))
    elif input_type == 'EmailInput':
        return forms.CharField(widget=forms.EmailInput(attrs=attrs))
    else:
        return forms.CharField(widget=forms.PasswordInput(attrs=attrs))
