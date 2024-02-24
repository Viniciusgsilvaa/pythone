from django.contrib import admin
from .models import Portifolio, Cargo, Funcionario, Sobre


@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = ('cabecalio', 'sublinha', 'sobre', 'imagem', 'criado', 'modificado', 'ativo')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'criado', 'modificado', 'ativo')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'imagem', 'facebook', 'x', 'instagram', 'criado', 'modificado', 'ativo')


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('data', 'cabecalio', 'sobre', 'imagem', 'criado', 'modificado', 'ativo')