from uuid import uuid4
from datetime import timedelta

from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now

from clients.models import User, EmailVerification


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


def code_and_expiration_for_email_verification():
    expiration = now() + timedelta(hours=12)
    code = uuid4()
    return code, expiration


def email_verify(kwargs, if_true):
    code = kwargs['code']
    email = kwargs['email']
    user = User.objects.get(email=email)
    verifications = EmailVerification.objects.filter(user=user, code=code)
    if verifications.exists() and not verifications.first().is_expired():
        user.is_verified = True
        user.save()
        return if_true
    else:
        return HttpResponseRedirect(reverse('index'))


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
