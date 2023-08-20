from django.db import models

from clients.models import User


class Order(models.Model):
    STATUS_CODE = {
        'CREATED': 0,
        'PAID': 1,
        'ON_WAY': 2,
        'DELIVERED': 3
    }
    ORDER_STATUSES = (
        (STATUS_CODE['CREATED'], 'Created'),
        (STATUS_CODE['PAID'], 'Paid'),
        (STATUS_CODE['ON_WAY'], 'On way'),
        (STATUS_CODE['DELIVERED'], 'Delivered')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_first_name = models.CharField(max_length=30)
    delivery_last_name = models.CharField(max_length=60)
    delivery_email = models.EmailField(max_length=128)
    delivery_address = models.CharField(max_length=256)
    cart = models.JSONField(default=dict)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUSES, default=STATUS_CODE['CREATED'])

    def __str__(self):
        return f'Order №{self.id} | {self.delivery_last_name} {self.delivery_first_name}'
