from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = (
        'id', 'status',
        ('delivery_first_name', 'delivery_last_name'),
        ('delivery_email', 'delivery_address'), 'cart', 'created_date')
    readonly_fields = ('id', 'created_date',)
