from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from products.models import Product


class IndexViewTestCase(TestCase):
    def test_view(self):
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'productsdump.json']

    def test_products_list(self):
        url = reverse('products:index')
        response = self.client.get(url)

        products = Product.objects.all()
        products_page_1 = products[:3]
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(products_page_1))
