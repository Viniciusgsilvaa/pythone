from django.db import models


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    
    class Meta:
        abstract = True

class Post(Base):

    nome = models.CharField('Nome', max_length=200)
    titulo = models.CharField('Titulo', max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.nome