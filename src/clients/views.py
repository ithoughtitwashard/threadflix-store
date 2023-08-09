from django.shortcuts import render

from clients.account_services import authentication_authorization
from clients.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            return authentication_authorization(request)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'clients/login.html', context)


def registration(request):
    return render(request, 'clients/registration.html')
