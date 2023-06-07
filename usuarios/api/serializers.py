from rest_framework import serializers
from usuarios.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua','bairro','numero']

"""
class UsuarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    class Meta:
        model = Usuario
        fields = ['id','email','first_name','last_name','cpf','tipo','endereco']

class FuncionarioSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(queryset=Endereco.objects.all())
    class Meta:
        model = Funcionario
        fields = ['id','email','first_name','last_name','cpf','endereco','data_de_contrato']

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)

        funcionario = Funcionario.objects.create(endereco=endereco, **validated_data)

        return funcionario"""