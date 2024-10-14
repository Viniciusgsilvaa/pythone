from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    
    class Meta:
        abstract = True

class Post(Base):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField('Nome', max_length=200)
    titulo = models.CharField('Titulo', max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.nome
    

class Perfil(Base):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    localizacao = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.usuario.username

    def get_seguindo(self):
        return User.objects.filter(seguidores__seguidor=self.usuario)
    
    def get_seguidores(self):
        return User.objects.filter(seguindo_usuario=self.usuario)

class Seguidor(Base):

    usuario = models.ForeignKey(User, related_name='seguindo', on_delete=models.CASCADE)
    seguidor = models.ForeignKey(User, related_name='seguidores', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('usuario', 'seguidor')
    
    def __str__(self):
        return self.usuario.username