from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index')
]
