# produtos/admin.py
from django.contrib import admin
from .models import Categoria, Produto

# Registra os modelos para que apareçam no /admin/
admin.site.register(Categoria)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Campos que aparecem na lista de produtos do painel Admin
    list_display = ('nome', 'codigo', 'categoria', 'preco', 'acabamento')
    # Permite pesquisar por nome ou código
    search_fields = ('nome', 'codigo')
    # Permite filtrar por categoria
    list_filter = ('categoria', 'acabamento')