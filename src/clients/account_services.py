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