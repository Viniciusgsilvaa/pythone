from django.urls import path
from .views import cliente, cadastro, cadastrados

urlpatterns = [
    path('cliente', cliente, name='cliente'),
    path('cadastro', cadastro,  name='cadastro'),
    path('cadastrados', cadastrados, name='cadastrados')
]