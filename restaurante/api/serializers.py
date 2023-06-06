from rest_framework import serializers
from restaurante.models import Carrinho, Produto, Restaurantes
from usuarios.api.serializers import FuncionarioSerializer, EnderecoSerializer, UsuarioSerializer
from usuarios.models import Endereco, Funcionario

class RestauranteSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer()
    endereco = EnderecoSerializer()
    class Meta:
        model = Restaurantes
        fields = ['id','nome','cnpj','endereco','funcionario']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(rua=endereco_data['rua'], bairro=endereco_data['bairro'], numero=endereco_data['numero'])

        funcionario_data = validated_data.pop('funcionario')
        funcionario = Funcionario.objects.create(**funcionario_data)

        restaurante = Restaurantes.objects.create(endereco=endereco, funcionario=funcionario, **validated_data)

        return restaurante
    
    

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id','nome','preco','ingredientes','quantidade']

class CarrinhoSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(read_only=True)
    cliente = UsuarioSerializer(read_only=True)
    class Meta:
        model = Carrinho
        fields = ['id','data','produtos','cliente']