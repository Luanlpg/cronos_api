from ..models import TeamMember
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import TeamMemberSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet para TeamMember.
    """
    permission_classes = [IsAuthenticated]
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
