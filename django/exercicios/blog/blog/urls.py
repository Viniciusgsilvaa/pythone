from django.urls import path
from .views import ListaPostagemView, CreatePostView, VotarPostView

urlpatterns = [
    path('post/', ListaPostagemView.as_view(), name='lista_postagens'),
    path('criar_post/', CreatePostView.as_view(), name='criar_post'),
    path('post/<int:post_id>/votar/<str:tipo_voto>/', VotarPostView.as_view(), name='votar_post')
]