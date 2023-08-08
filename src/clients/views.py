from django.shortcuts import render


def login(request):
    return render(request, 'clients/login.html')


def registration(request):
    return render(request, 'clients/registration.html')
