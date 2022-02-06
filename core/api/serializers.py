from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer de usuário."""
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']
