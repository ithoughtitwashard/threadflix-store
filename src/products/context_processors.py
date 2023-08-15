from django.db.models import F

from products.models import Cart


def carts(request):
    user = request.user
    return {'carts': Cart.objects.filter(user=user).select_related('product').only('product__name',
                                                                                   'product__description',
                                                                                   'product__price',
                                                                                   'id',
                                                                                   'quantity').annotate(
        total=F('quantity') * F('product__price')) if user.is_authenticated else []}
