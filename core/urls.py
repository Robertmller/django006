from django.urls import path, include

from .views import index, contato, produto

from .viewsets import ProdutoViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)



urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('api/v1/', include(router.urls)),
    #path('avaliacao/<int:pk>', avaliacao, name='avaliação')

]
