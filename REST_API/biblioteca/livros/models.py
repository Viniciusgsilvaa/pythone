from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Livro(Base):
    titulo = models.CharField(max_length=250)
    autor = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
    
    def __str__(self):
        return self.titulo


class Avaliacoes(Base):
    titulo = models.ForeignKey(Livro, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'titulo']

    
    def __str__(self):
       return f'{self.nome} avaliou o curso: {self.titulo} com a nota: {self.avaliacao}'


    
