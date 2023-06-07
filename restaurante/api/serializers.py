from rest_framework import serializers
from restaurante.models import Carrinho, Produto, Restaurantes
from usuarios.models import Endereco
from usuarios.api.serializers import EnderecoSerializer

class RestauranteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Restaurantes
        fields = ['id','nome','cnpj','endereco']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(rua=endereco_data['rua'], bairro=endereco_data['bairro'], numero=endereco_data['numero'])

        restaurante = Restaurantes.objects.create(endereco=endereco, **validated_data)

        return restaurante
    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco','ingredientes','quantidade']

class CarrinhoSerializer(serializers.ModelSerializer):
    """produtos = ProdutoSerializer(read_only=True)"""
    class Meta:
        model = Carrinho
        fields = ['id','data','produtos']

