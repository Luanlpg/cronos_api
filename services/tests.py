from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from .models import Service


class ServiceTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='zzm', password='1234xxxx')
        self.user.is_admin = True
        self.user.save()

    def test_list_services(self):
        """
        Teste de listagem de serviços.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/services/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_service(self):
        """
        Teste de criação de serviço.
        """
        data = {
            "name": "criação de site",
            "description": "criação de site",
            "category": 'dev',
            "price": 10.00
        }
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/services/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)
