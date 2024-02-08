from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

admin.site.register(Produtos, ProdutosAdmin)

