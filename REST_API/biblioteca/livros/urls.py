from django.urls import path
from .views import AvaliacaoAPIView, LivroAPIView

urlpatterns = [
    path('livro/', LivroAPIView.as_view(), name='livro'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes')
]