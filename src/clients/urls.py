from django.urls import path

from clients.views import login, registration

app_name = 'clients'

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', registration, name='registration'),
]
