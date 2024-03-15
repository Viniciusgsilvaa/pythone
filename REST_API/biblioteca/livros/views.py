from .models import Livro, Avaliacoes
from .serializers import AvaliacaoSerializer, LivroSerializer
from rest_framework import generics
from rest_framework.generics import get_object_or_404


class LivrosAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('livro_pk'):
            return self.queryset.filter(titulo_id=self.kwargs.get('livro_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('livro_pk'):
            return get_object_or_404(self.get_queryset(), titulo_id=self.kwargs.get('livro_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
 