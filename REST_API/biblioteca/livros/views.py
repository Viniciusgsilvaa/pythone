from .models import Livro, Avaliacoes
from .serializers import AvaliacaoSerializer, LivroSerializer
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import EhSuperUser


"""
API V1
"""

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


"""
API V2
"""

class LivroViewSet(viewsets.ModelViewSet):
    permission_classes = (EhSuperUser, permissions.DjangoModelPermissions, )
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacoes.objects.filter(titulo_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
        
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer