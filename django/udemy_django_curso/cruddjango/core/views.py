from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name= 'index.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'
