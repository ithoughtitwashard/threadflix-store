from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import ImageField, FileInput

from clients.account_services import register_form_fields, login_form_fields, profile_form_fields_without_image, \
    code_and_expiration_for_email_verification
from clients.models import User, EmailVerification


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

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        code, expiration = code_and_expiration_for_email_verification()
        record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
        record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    first_name, last_name, username, email = profile_form_fields_without_image()
    image = ImageField(widget=FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
