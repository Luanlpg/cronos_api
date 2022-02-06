from ..models import Post
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Post.
    """
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
