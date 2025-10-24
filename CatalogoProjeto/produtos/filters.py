# produtos/filters.py
import django_filters
from .models import Produto, Categoria

class ProdutoFilter(django_filters.FilterSet):
    # Permite filtrar por categorias (exibido como um menu dropdown)
    categoria = django_filters.ModelChoiceFilter(
        queryset=Categoria.objects.all(),
        empty_label="Todas as Categorias"
    )

    # Permite buscar por texto no campo nome
    nome = django_filters.CharFilter(
        field_name='nome', 
        lookup_expr='icontains', # Busca insensível a maiúsculas/minúsculas
        label='Buscar Produto'
    )

    class Meta:
        model = Produto
        fields = ['categoria', 'acabamento', 'nome']