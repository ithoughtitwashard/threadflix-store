from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ImageField, FileInput

from clients.account_services import register_form_fields, login_form_fields, profile_form_fields_without_image
from clients.models import User


class UserLoginForm(AuthenticationForm):
    username, password = login_form_fields()

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name, last_name, username, email, password1, password2 = register_form_fields()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name, last_name, username, email = profile_form_fields_without_image()
    image = ImageField(widget=FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
