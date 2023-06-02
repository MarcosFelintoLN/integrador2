from rest_framework import serializers
from restaurante.models import Carrinho, Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco','ingredientes','quantidade']

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        produtos = ProdutoSerializer(read_only=True)
        fields = ['id','data','produtos',]