# produtos/views.py
from django.shortcuts import render
from .models import Produto
from .filters import ProdutoFilter

def catalogo(request):
    # 1. Pega todos os produtos
    produtos = Produto.objects.all() 

    # 2. Aplica o filtro de busca (usa os dados da URL)
    filtro = ProdutoFilter(request.GET, queryset=produtos)

    context = {
        'filtro': filtro,
        'produtos': filtro.qs, # A lista de produtos filtrados
    }
    return render(request, 'catalogo.html', context)