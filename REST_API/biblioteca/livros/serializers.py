from rest_framework import serializers
from .models import Livro, Avaliacoes


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model =  Avaliacoes
        fields = (
            'id',
            'titulo',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'atualizacao',
            'ativo'
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliacao precisa ser entre 1 a 5')

class LivroSerializer(serializers.ModelSerializer):
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacoes-detail')
    
    class Meta:
        model = Livro
        fields = (
            'id',
            'titulo',
            'autor',
            'descricao',
            'preco',
            'atualizacao',
            'ativo',
            'avaliacoes'

        )