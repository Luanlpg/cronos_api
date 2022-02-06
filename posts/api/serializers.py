from ..models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Serializer de postagem."""
    class Meta:
        model = Post
        fields = '__all__'
