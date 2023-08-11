from django.urls import path

from products.views import products, add_to_cart, remove_from_cart

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>', products, name='category'),
    path('page/<int:page_num>', products, name='paginator'),
    path('carts/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('carts/remove/<int:cart_id>/', remove_from_cart, name='cart_remove'),
]
