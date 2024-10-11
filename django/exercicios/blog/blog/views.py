from typing import Any
from django.views.generic import TemplateView, CreateView
from .models import Post
from .form import PostForm
from django.urls import reverse_lazy

class ListaPostagemView(TemplateView):
    template_name = 'lista_postagens.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa a queryset com todas as postagens
        context['postagens'] = Post.objects.all()    
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'criar_post.html'
    success_url = reverse_lazy('lista_postagens')
    
