from rest_framework import serializers
from usuarios.models import Endereco, Usuario, Funcionario

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua','bairro','numero']

class UsuarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    class Meta:
        model = Usuario
        fields = ['id','email','first_name','last_name','cpf','tipo','endereco']

class FuncionarioSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    class Meta:
        model = Funcionario
        fields = ['id','email','first_name','last_name','cpf','endereco','data_de_contrato']