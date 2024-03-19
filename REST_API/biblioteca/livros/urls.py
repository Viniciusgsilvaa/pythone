from django.urls import path
from .views import AvaliacoesAPIView, LivroAPIView, AvaliacaoAPIView, LivrosAPIView, LivroViewSet, AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('livro', LivroViewSet, basename='livro')
router.register('avaliacoes', AvaliacaoViewSet, basename='avaliacoes')

urlpatterns = [
    path('livros/', LivrosAPIView.as_view(), name='livros'),
    path('livro/<int:pk>/', LivroAPIView.as_view(), name='livro'),
    path('livros/<int:livro_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='livro_avaliacao'),
    path('livros/<int:livro_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]