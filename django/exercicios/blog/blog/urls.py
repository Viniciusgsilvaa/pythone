from django.urls import path
from .views import ListaPostagemView, CreatePostView

urlpatterns = [
    path('post/', ListaPostagemView.as_view(), name='lista_postagens'),
    path('criar_post/', CreatePostView.as_view(), name='criar_post'),
    
]