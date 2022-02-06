from ..models import TeamMember
from rest_framework import serializers


class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer de membro da equipe."""
    class Meta:
        model = TeamMember
        fields = '__all__'
