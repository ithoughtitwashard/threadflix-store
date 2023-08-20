from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from clients.models import User
from orders.models import Order


class OrderCreateViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('orders:create')
        self.user_data = {
            'first_name': 'Thread',
            'last_name': 'Flix',
            'username': 'new_test_user',
            'email': 'test@gmail.com',
            'password1': 'bimbambum',
            'password2': 'bimbambum',
        }
        self.order_data = {
            'delivery_first_name': 'Thread',
            'delivery_last_name': 'Flix',
            'delivery_email': 'test@gmail.com',
            'delivery_address': 'bimbambum',
        }

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'orders/order-create.html')

    def test_creating(self):
        redirect_url = reverse('orders:create')
        response_user = self.client.post(reverse('clients:registration'), data=self.user_data)
        self.client.login(username=self.user_data['username'], password=self.user_data['password1'])

        order = Order.objects.filter(id=1)
        self.assertFalse(order.exists())

        response = self.client.post(self.url, data=self.order_data)

        order = Order.objects.filter(id=1)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(order.exists())
        self.assertRedirects(response, redirect_url)
