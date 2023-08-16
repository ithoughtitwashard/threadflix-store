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

    def test_category_products_list(self):
        url_cloth = reverse('products:category', kwargs={'category_id': 1})  # Cloth
        url_accessories = reverse('products:category', kwargs={'category_id': 3})  # Accessories
        response_cloth = self.client.get(url_cloth)
        response_accessories = self.client.get(url_accessories)

        self.assertEqual(response_cloth.status_code, HTTPStatus.OK)
        self.assertEqual(response_accessories.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response_cloth, 'products/products.html')
        self.assertTemplateUsed(response_accessories, 'products/products.html')

        products_cloth = Product.objects.filter(category_id=1)
        products_accessories = Product.objects.filter(category_id=3)

        self.assertEqual(list(response_cloth.context_data['object_list']), list(products_cloth))
        self.assertEqual(list(response_accessories.context_data['object_list']), list(products_accessories))
