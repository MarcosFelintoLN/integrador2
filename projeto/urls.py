from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from restaurante.api.viewsets import ProdutoViewSet, CarrinhoViewSet, RestauranteViewSet
from usuarios.api.viewsets import ClienteViewSet

router = routers.SimpleRouter()
router.register('carrinho',CarrinhoViewSet) #ok
router.register('produto',ProdutoViewSet) #ok
"""router.register('cliente',ClienteViewSet) #erro"""
router.register('restaurante',RestauranteViewSet) #ok


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api_schema', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(template_name='docs.html',extra_context={'schema_url':'api_schema'}))
    
]
