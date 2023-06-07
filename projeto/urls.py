from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurante.api.viewsets import ProdutoViewSet, CarrinhoViewSet, RestauranteViewSet
#from usuarios.api.viewsets import UsuarioViewSet, FuncionarioViewSet

router = routers.SimpleRouter()
router.register('carrinho',CarrinhoViewSet) #ok
router.register('produto',ProdutoViewSet) #ok
#router.register('usuario',UsuarioViewSet) #erro
router.register('restaurante',RestauranteViewSet) #ok
#router.register('funcionario',FuncionarioViewSet) #erro
"""router.register('endereco',EnderecoViewSet)"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
    
]
