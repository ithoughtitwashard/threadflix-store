from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from clients.account_services import user_authentication_authorization
from clients.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            return user_authentication_authorization(request)
    else:
        form = UserLoginForm()
    content = {'title': 'Sign in to ThreadFlix',
               'form': form}
    return render(request, 'clients/login.html', content)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful registration!')
            return HttpResponseRedirect(reverse('clients:login'))
    else:
        form = UserRegisterForm()
    content = {'title': 'Sign up with ThreadFlix',
               'form': form}
    return render(request, 'clients/registration.html', content)


def profile_page(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clients:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    content = {'title': 'My profile',
               'form': form
               }
    return render(request, 'clients/profile.html', content)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))