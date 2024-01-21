from django.urls import path
from .views import cliente, cadastro

urlpatterns = [
    path('cliente', cliente, name='cliente'),
    path('cadastro', cadastro,  name='cadastro')
]