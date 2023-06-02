from rest_framework.viewsets import ModelViewSet
from restaurante.models import Carrinho, Produto
from restaurante.api.serializers import CarrinhoSerializer, ProdutoSerializer

class CarrinhoViewSet(ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer