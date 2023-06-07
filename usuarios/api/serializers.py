from rest_framework import serializers
from usuarios.models import Endereco, Cliente

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua','bairro','numero']


class ClienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Cliente
        fields = ['id','email','first_name','last_name','cpf','endereco','password1','password2']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)

        cliente = Cliente.objects.create(endereco=endereco, **validated_data)

        return cliente