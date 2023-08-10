from django.urls import path

from products.views import products, add_to_cart, remove_from_cart

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('carts/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('carts/remove/<int:cart_id>/', remove_from_cart, name='cart_remove'),
]
