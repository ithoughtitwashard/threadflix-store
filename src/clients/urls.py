from django.urls import path

from clients.views import login, registration, profile_page

app_name = 'clients'

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', registration, name='registration'),
    path('profile/', profile_page, name='profile'),
]
