from django.db.models import F, Sum

from products.models import Cart


def carts(request):
    user = request.user
    carts_queryset = Cart.objects.filter(user=user.id).select_related('product').only('product__name',
                                                                                      'product__description',
                                                                                      'product__price',
                                                                                      'id',
                                                                                      'quantity').annotate(
        total=F('quantity') * F('product__price'))

    if not carts_queryset:
        total = 0
    else:
        total = carts_queryset.aggregate(check_sum=Sum('total'))['check_sum']

    return {'carts': carts_queryset if user.is_authenticated else [],
            'total': total if user.is_authenticated else 0
            }
