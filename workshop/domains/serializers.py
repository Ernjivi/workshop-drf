from rest_framework.serializers import ModelSerializer
from domains.models import Client, Domain


class DomainSerializer(ModelSerializer):
    """
    DomainSerializer.
    """

    class Meta:
        model = Domain
        fields = ['id', 'name', 'ip', 'client', 'foo']



class ClientSerializer(ModelSerializer):
    """
    ClientSerializer.
    """

    domains = DomainSerializer(many=True,
        read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'domains']