from django.contrib import admin
from .models import Post, Perfil, Seguidor, Comentario, VotoComentario

admin.site.register(Post)
admin.site.register(Perfil)
admin.site.register(Seguidor)
admin.site.register(Comentario)
admin.site.register(VotoComentario)


