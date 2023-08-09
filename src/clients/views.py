from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from clients.account_services import user_authentication_authorization
from clients.forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            return user_authentication_authorization(request)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'clients/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clients:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'clients/registration.html', context)
