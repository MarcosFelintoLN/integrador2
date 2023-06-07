from rest_framework.viewsets import ModelViewSet
from usuarios.api.serializers import EnderecoSerializer, ClienteSerializer
from usuarios.models import Endereco, Cliente

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer()

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer()