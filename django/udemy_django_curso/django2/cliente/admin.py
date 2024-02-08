from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClinteAdmin(admin.ModelAdmin):
    list_display= ('nome', 'email', 'cpf', 'senha', 'criado', 'modificado', 'ativo')