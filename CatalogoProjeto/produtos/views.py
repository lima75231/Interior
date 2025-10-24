from django.shortcuts import render
from .models import Produto
from .filters import ProdutoFilter

def catalogo(request):
    # 1. Pega todos os produtos
    produtos = Produto.objects.all() 

    # 2. Aplica os filtros (categoria, acabamento, busca)
    filtro = ProdutoFilter(request.GET, queryset=produtos)

    context = {
        'filtro': filtro,
        'produtos': filtro.qs, # Resultados após o filtro
        'categorias': Categoria.objects.all(), # Para exibir as abas laterais
    }
    return render(request, 'catalogo.html', context)