from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    
    
    class Meta:
        abstract = True

''
class Post(Base):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField('Nome', max_length=200)
    titulo = models.CharField('Titulo', max_length=100)
    conteudo = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def adicionar_voto(self, usuario, tipo_voto):
        # Verificar se o usuário já votou nesse post
        voto_existente = VotoPost.objects.filter(post=self, usuario=usuario).first()

        if voto_existente:
            # Se o usuário já votou e o tipo de voto é o mesmo, remova o voto
            if voto_existente.tipo_voto == tipo_voto:
                voto_existente.delete()
                if tipo_voto == 'like':
                    self.likes -= 1
                else:
                    self.dislikes -= 1
            # Se o voto for diferente, troque o tipo de voto
            else:
                if voto_existente.tipo_voto == 'like':
                    self.likes -= 1
                    self.dislikes += 1
                else:
                    self.likes += 1
                    self.dislikes -= 1
                voto_existente.tipo_voto = tipo_voto
                voto_existente.save()
        else:
            # Se não houver voto, crie um novo
            VotoPost.objects.create(post=self, usuario=usuario, tipo_voto=tipo_voto)
            if tipo_voto == 'like':
                self.likes += 1
            else:
                self.dislikes += 1

        # Salvar as mudanças no post
        self.save()

    def __str__(self):
        return self.nome
    

class VotoPost(Base):
    post = models.ForeignKey(Post, related_name='votos', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_voto = models.CharField(max_length=10, choices=[('like', 'Like'), ('dislike', 'Dislike')])

    class Meta:
        unique_together = ('post', 'usuario')  # Cada usuário pode votar apenas uma vez em cada post

    def __str__(self):
        return f'{self.usuario} - {self.tipo_voto} - {self.post.titulo}'


class Comentario(Base):
    post = models.ForeignKey(Post,  related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def adicionar_voto(self, usuario, tipo_voto):
        # Verificar se o usuário já votou no comentário
        voto_existente = VotoComentario.objects.filter(comentario=self, usuario=usuario).first()

        if voto_existente:
            # Se o usuário já votou e o voto for igual ao atual, remova o voto
            if voto_existente.tipo_voto == tipo_voto:
                voto_existente.delete()
                if tipo_voto == 'like':
                    self.likes -= 1
                else:
                    self.dislikes -= 1
            # Se o voto for diferente, atualize o tipo de voto
            else:
                if voto_existente.tipo_voto == 'like':
                    self.likes -= 1
                    self.dislikes += 1
                else:
                    self.likes += 1
                    self.dislikes -= 1
                voto_existente.tipo_voto = tipo_voto
                voto_existente.save()
        else:

            VotoComentario.objects.create(comentario=self, usuario=usuario, tipo_voto=tipo_voto)
            if tipo_voto == 'like':
                self.likes += 1
            else:
                self.dislikes += 1
            

        self.save()
        


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

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    localizacao = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    reputacao = models.IntegerField(default=0)

    def atualizar_reputacao(self):
        respostas = self.usuario.respostas.all()
        reputacao = sum([resposta.votos_positivos - resposta.voto_negativo for resposta in respostas])
        self.reputacao = reputacao
        self.save()

    def __str__(self):
        return f'Perfil de {self.usuario.username} com reputação {self.reputacao}'

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


class Pergunta(Base):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    melhor_resposta = models.OneToOneField(
        'Resposta', null=True, blank=True, on_delete=models.SET_NULL,
        related_name='melhor_resposta_da_pergunta'
    )

    def __str__(self):
        return self.usuario.titulo


class Resposta(Base):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    votos_positivos = models.IntegerField(default=0)
    votos_negativos = models.IntegerField(default=0)

    def votar(self, usuario, tipo_voto):
        """Método para adicionar ou remover voto positivo ou negativo."""
        voto_existente = VotoResposta.objects.filter(resposta=self, usuario=usuario).first()

        if voto_existente:
            # Se o voto é do mesmo tipo, remove o voto
            if voto_existente.tipo_voto == tipo_voto:
                voto_existente.delete()
                if tipo_voto == 'positivo':
                    self.votos_positivos -= 1
                else:
                    self.votos_negativos -= 1
            # Se o voto é diferente, troca o voto
            else:
                if voto_existente.tipo_voto == 'positivo':
                    self.votos_positivos -= 1
                    self.votos_negativos += 1
                else:
                    self.votos_positivos += 1
                    self.votos_negativos -= 1
                voto_existente.tipo_voto = tipo_voto
                voto_existente.save()
        else:
            # Cria um novo voto se não existir
            VotoResposta.objects.create(resposta=self, usuario=usuario, tipo_voto=tipo_voto)
            if tipo_voto == 'positivo':
                self.votos_positivos += 1
            else:
                self.votos_negativos += 1

        self.save()
        self.usuario.profile.atualizar_reputacao()

    def __str__(self):
        return f'Resposta de {self.usuario.username} para "{self.pergunta.titulo}"'


class VotoResposta(Base):
    VOTO_CHOICES = [
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo'),
    ]
    respostas = models.ForeignKey(Resposta, on_delete=models.CASCADE, related_name='votos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_voto = models.CharField(max_length=8, choices=VOTO_CHOICES)
    

    def __str__(self):
        return f'Voto de {self.usuario.username} na resposta {self.resposta.id}'