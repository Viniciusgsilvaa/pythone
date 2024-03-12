from .models import Livro, Avaliacoes
from .serializers import AvaliacaoSerializer, LivroSerializer
from rest_framework import generics


class LivroAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class AvaliacaoAPIView(generics.ListCreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
