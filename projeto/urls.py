from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurante.api.viewsets import ProdutoViewSet, CarrinhoViewSet, RestauranteViewSet
from usuarios.api.viewsets import UsuarioViewSet, FuncionarioViewSet, EnderecoViewSet

router = routers.SimpleRouter()
router.register('carrinho',CarrinhoViewSet)
router.register('produto',ProdutoViewSet)
router.register('usuario',UsuarioViewSet)
router.register('restaurante',RestauranteViewSet)
router.register('funcionario',FuncionarioViewSet)
router.register('endereco',EnderecoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
    
]
