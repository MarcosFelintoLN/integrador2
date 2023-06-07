from django.db import models
from django.contrib.auth.models import AbstractUser

class Endereco(models.Model):
    rua = models.CharField(verbose_name="Rua",max_length=100)
    bairro = models.CharField(verbose_name="Bairro",max_length=100)
    numero = models.IntegerField(verbose_name="Número")
    
class Cliente(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email",unique=True)
    cpf = models.CharField(verbose_name="CPF", max_length=12)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['cpf','endereco']

    """def create_carrinho(self):
        from restaurante.models import Carrinho
        return Carrinho.objects.create(cliente=self)"""
