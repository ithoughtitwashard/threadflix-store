from django.shortcuts import render

from .models import Category, Product
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
