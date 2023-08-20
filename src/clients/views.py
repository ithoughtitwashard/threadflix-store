from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from clients.account_services import email_verify
from clients.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from clients.models import User
from default.views import TitleMixin


class UserLoginView(LoginView):
    template_name = 'clients/login.html'
    form_class = UserLoginForm


class UserRegisterView(SuccessMessageMixin, TitleMixin, CreateView):
    title = 'Sign up with ThreadFlix'
    model = User
    form_class = UserRegisterForm
    template_name = 'clients/registration.html'
    success_url = reverse_lazy('clients:login')
    success_message = 'Successful registration!'


class UserProfileView(TitleMixin, UpdateView):
    title = 'My profile'
    model = User
    form_class = UserProfileForm
    template_name = 'clients/profile.html'

    def get_success_url(self):
        return reverse('clients:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Email verification'
    template_name = 'clients/email_verification.html'

    def get(self, request, *args, **kwargs):
        get = super(EmailVerificationView, self).get(request, *args, **kwargs)
        return email_verify(kwargs=kwargs, if_true=get)
