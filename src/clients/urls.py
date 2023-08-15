from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from clients.views import UserRegisterView, UserProfileView, UserLoginView, EmailVerificationView

app_name = 'clients'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', UserRegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='verification'),
]
