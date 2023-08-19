from django.urls import path

from orders.views import OrderCreateView

app_name = 'orders'

urlpatterns = [
    path('', OrderCreateView.as_view(), name='create'),

]
