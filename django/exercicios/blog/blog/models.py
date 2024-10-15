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


class Comentario(Base):
    post = models.ForeignKey(Post,  related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comentário de {self.usuario} no post {self.post.titulo}' 


class VotoComentario(Base):
    comentario = models.ForeignKey(Comentario, related_name='votos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_voto = models.CharField(max_length=10, choices=[('like', 'Like'), ('dislike', 'Dislike')])
    
    class Meta:
        unique_together = ('comentario', 'usuario')  # Garante que o usuário só possa votar uma vez no comentário

    def __str__(self):
        return f'{self.usuario} votou {self.tipo_voto} no comentário {self.comentario.id}'

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