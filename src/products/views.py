from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Category, Product, Cart


def index(request):
    content = {
        'title': 'ThreadFlix',
    }
    return render(request, 'products/index.html', content)


def products(request):
    products_queryset = Product.objects.all()
    categories_queryset = Category.objects.all().order_by('id')
    content = {
        'title': 'ThreadFlix catalogue',
        'products': products_queryset,
        'categories': categories_queryset
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
