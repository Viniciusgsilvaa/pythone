from django.contrib import admin
from .models import Post, Perfil, Seguidor, Comentario, VotoComentario, VotoResposta, VotoPost, Pergunta, Resposta

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Sobre o Usuario', {'fields': ['usuario', 'nome']}),
        ('Sobre o Post', {'fields': ['titulo', 'conteudo']}),
        ('Avaliação do Perfil', {'fields': ['likes', 'dislikes']})
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Perfil)
admin.site.register(Seguidor)
admin.site.register(Comentario)
admin.site.register(VotoComentario)
admin.site.register(VotoResposta)
admin.site.register(VotoPost)
admin.site.register(Pergunta)
admin.site.register(Resposta)


