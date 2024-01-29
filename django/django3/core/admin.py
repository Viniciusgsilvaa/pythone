from django.contrib import admin
from .models import Servico, Cargo, Equipe


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display= ('servico', 'descricao', 'icone', 'criados', 'modificado', 'ativo')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'criados', 'modificado', 'ativo')


@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'bio', 'imagem', 'facebook', 'x', 'instagram', 'criados', 'modificado', 'ativo')
