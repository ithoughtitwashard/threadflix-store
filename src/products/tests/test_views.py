from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from products.models import Product, Category


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

        self._status_ok_and_products_template_test(response)
        self.assertEqual(list(response.context_data['object_list']), list(products_page_1))

    def test_category_products_list(self):
        category_cloth = Category.objects.get(id=1)
        category_accessories = Category.objects.get(id=3)

        url_cloth = reverse('products:category', kwargs={'category_id': category_cloth.id})
        url_accessories = reverse('products:category', kwargs={'category_id': category_accessories.id})

        response_cloth = self.client.get(url_cloth)
        response_accessories = self.client.get(url_accessories)

        self._status_ok_and_products_template_test(response_cloth)
        self._status_ok_and_products_template_test(response_accessories)

        products_cloth = Product.objects.filter(category_id=1)
        products_accessories = Product.objects.filter(category_id=3)

        self.assertEqual(list(response_cloth.context_data['object_list']), list(products_cloth))
        self.assertEqual(list(response_accessories.context_data['object_list']), list(products_accessories))

    def test_paginator_products_list(self):
        url_page_1 = reverse('products:paginator', kwargs={'page': 1})
        url_page_2 = reverse('products:paginator', kwargs={'page': 2})

        response_page_1 = self.client.get(url_page_1)
        response_page_2 = self.client.get(url_page_2)

        self._status_ok_and_products_template_test(response_page_1)
        self._status_ok_and_products_template_test(response_page_2)

        products = Product.objects.all()
        products_page_1 = products[:3]
        products_page_2 = products[3:]

        self.assertEqual(list(response_page_1.context_data['object_list']), list(products_page_1))
        self.assertEqual(list(response_page_2.context_data['object_list']), list(products_page_2))

    def _status_ok_and_products_template_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/products.html')
