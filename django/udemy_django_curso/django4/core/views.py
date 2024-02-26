from typing import Any
from django.views.generic import TemplateView
from .models import Sobre, Portifolio, Funcionario


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.all()
        context['portifolio'] = Portifolio.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        return context