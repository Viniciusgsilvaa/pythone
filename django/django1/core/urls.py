from django.urls import path
from .views import index, contato

urlpatterns = [
    path('index', index),
    path('contato', contato)
]