from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class IndexViewTestCase(TestCase):
    def test_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'products/index.html')