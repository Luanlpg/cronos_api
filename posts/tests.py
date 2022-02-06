from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from .models import Post


class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='zzm', password='1234xxxx')
        self.user.is_admin = True
        self.user.save()

    def test_list_posts(self):
        """
        Teste de listagem de postagens.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        """
        Teste de criação de postagem.
        """
        data = {
            "title": "Teste de postagem",
            "content": "Conteúdo da postagem"
        }
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/posts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
