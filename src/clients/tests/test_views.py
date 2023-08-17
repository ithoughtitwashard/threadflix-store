from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from clients.models import User, EmailVerification


class UserRegisterViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('clients:registration')
        self.user_data = {
            'first_name': 'Thread',
            'last_name': 'Flix',
            'username': 'test_user',
            'email': 'test@gmail.com',
            'password1': 'bimbambum',
            'password2': 'bimbambum',
        }

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'clients/registration.html')

    def test_register(self):
        redirect_url = reverse('clients:login')
        username = self.user_data['username']

        user = User.objects.filter(username=username)
        self.assertFalse(user.exists())

        response = self.client.post(self.url, data=self.user_data)

        user = User.objects.filter(username=username)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_url)
        self.assertTrue(user.exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())

    def test_user_exist_error(self):
        username = self.user_data['username']
        user = User.objects.create(username=username)
        error_msg = 'A user with that username already exists.'
        response = self.client.post(self.url, data=self.user_data)

        self.assertContains(response, error_msg, html=True)
