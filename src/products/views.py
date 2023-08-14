from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView

from default.views import TitleMixin
from .models import Category, Product, Cart


class IndexView(TitleMixin, TemplateView):
    title = 'ThreadFlix'
    template_name = 'products/index.html'


class ProductsListView(TitleMixin, ListView):
    title = 'ThreadFlix catalogue'
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        queryset = queryset.filter(category_id=category_id) if category_id else queryset
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        categories_queryset = Category.objects.all().order_by('id')
        context['categories'] = categories_queryset
        return context


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
