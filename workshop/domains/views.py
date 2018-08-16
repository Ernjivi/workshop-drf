from rest_framework.viewsets import ModelViewSet
from domains.models import Domain, Client
from domains.serializers import (
    DomainSerializer,
    ClientSerializer
)


class ClientViewSet(ModelViewSet):
    """
    Client ViewSet.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DomainViewSet(ModelViewSet):
    """
    Domain ViewSet.
    """

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    def perform_create(self, serializer):
        serializer.save(foo=1)
