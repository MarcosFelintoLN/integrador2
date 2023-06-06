from rest_framework import serializers
from restaurante.models import Carrinho, Produto, Restaurantes
from usuarios.api.serializers import FuncionarioSerializer, EnderecoSerializer

class RestauranteSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)
    endereco = EnderecoSerializer(read_only=True)
    class Meta:
        model = Restaurantes
        fields = ['id','nome','cnpj','endereco','funcionario']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco','ingredientes','quantidade']

class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(read_only=True)
    class Meta:
        model = Carrinho
        fields = ['id','data','produtos','cliente']