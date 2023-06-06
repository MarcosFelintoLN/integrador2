from django.db import models
from usuarios.models import Endereco, Funcionario, Usuario

class Restaurantes(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=100)
    cnpj = models.CharField(verbose_name="CNPJ",max_length=20)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=50)
    preco = models.FloatField(verbose_name="Preço")
    ingredientes = models.CharField(verbose_name="Ingredientes",max_length=150)
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)

    def __str__(self):
        return self.nome
    
class Carrinho(models.Model):
    produtos = models.ManyToManyField(Produto)
    data = models.DateField(auto_now_add=True)
    cliente = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='carrinho',default=True)
