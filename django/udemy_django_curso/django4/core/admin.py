from django.contrib import admin
from .models import Portifolio


@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = ('cabecalio', 'sublinha', 'sobre', 'imagem', 'criado', 'modificado', 'ativo')
