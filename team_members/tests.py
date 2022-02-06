from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from .models import TeamMember


class TeamMemberTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='zzm', password='1234xxxx')
        self.user.is_admin = True
        self.user.save()

    def test_list_team_members(self):
        """
        Teste de listagem de membros da equipe.
        """
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/team-members/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team_member(self):
        """
        Teste de criação de membro da equipe.
        """
        data = {
            "first_name": "zezin",
            "last_name": "da silva",
            "email": 'ze@zinho.com',
            "phone": '11-1111-1111',
            "position": 'CTO',
            "bio": 'eu nasci no brasil e bla bla bla...'
        }
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/team-members/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TeamMember.objects.count(), 1)
