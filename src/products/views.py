from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Category, Product, Cart


def index(request):
    content = {
        'title': 'ThreadFlix',
    }
    return render(request, 'products/index.html', content)


def products(request, category_id=None, page_num=1):
    categories_queryset = Category.objects.all().order_by('id')
    products_queryset = Product.objects.filter(category=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products_queryset, per_page=3)
    products_paginator = paginator.page(page_num)

    content = {
        'title': 'ThreadFlix catalogue',
        'categories': categories_queryset,
        'products': products_paginator
    }
    return render(request, 'products/products.html', content)


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    carts = Cart.objects.filter(user=request.user, product=product)

    if not carts.exists():
        Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_from_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
