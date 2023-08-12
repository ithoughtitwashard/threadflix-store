from django.urls import path

from products.views import ProductsListView, add_to_cart, remove_from_cart

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>', ProductsListView.as_view(), name='category'),
    path('page/<int:page>', ProductsListView.as_view(), name='paginator'),
    path('carts/add/<int:product_id>/', add_to_cart, name='cart_add'),
    path('carts/remove/<int:cart_id>/', remove_from_cart, name='cart_remove'),
]
