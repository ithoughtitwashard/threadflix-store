from django import forms

from orders.models import Order
from orders.order_services import order_form_fields


class OrderCreateForm(forms.ModelForm):
    delivery_first_name, delivery_last_name, delivery_email, delivery_address = order_form_fields()

    class Meta:
        model = Order
        fields = ('delivery_first_name', 'delivery_last_name', 'delivery_email', 'delivery_address')
