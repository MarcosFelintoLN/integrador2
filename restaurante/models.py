from django.db import models

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome",max_length=50)
    preco = models.FloatField(verbose_name="Preço")
    ingredientes = models.CharField(verbose_name="Ingredientes",max_length=150)
    quantidade = models.IntegerField(verbose_name="Quantidade", default=1)

    def __str__(self):
        return self.nome
    
class Carrinho(models.Model):
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)