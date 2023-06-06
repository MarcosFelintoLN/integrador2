from rest_framework.viewsets import ModelViewSet
from usuarios.models import Usuario, Endereco, Funcionario
from usuarios.api.serializers import UsuarioSerializer,EnderecoSerializer, FuncionarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer()

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer()

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer()