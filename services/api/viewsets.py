from ..models import Service
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Service.
    """
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
