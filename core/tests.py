from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class UserTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='zzm', password='1234xxxx')
        self.user.is_admin = True
        self.user.save()

    def test_list_users(self):
        """
        Teste de listagem de usuários.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        """
        Teste de criação de usuário.
        """
        data = {
            "username": "teste",
            "email": "teste@teste.com",
            "is_staff": False
        }
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # 1 user created in setUp()
        self.assertEqual(User.objects.get(
            username='teste').email, 'teste@teste.com')
