from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from default.views import TitleMixin
from products.models import Cart


class OrderCreateView(TitleMixin, ListView):
    title = 'Make an order'
    model = Cart
    template_name = 'orders/order-create.html'
