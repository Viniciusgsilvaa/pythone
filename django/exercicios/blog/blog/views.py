from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, View
from .models import Post, Comentario
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


class VotarPostView(LoginRequiredMixin, View):
    
    def post(self, request, post_id, tipo_voto):
        # Buscar o post pelo ID, ou retornar 404 se não encontrar
        post = get_object_or_404(Post, id=post_id)

        # Verificar se o tipo de voto é válido (like ou dislike)
        if tipo_voto in ['like', 'dislike']:
            post.adicionar_voto(request.user, tipo_voto)  # Função existente no modelo Post

        # Redirecionar para a página de detalhes do post
        return redirect('lista_postagens')
    
