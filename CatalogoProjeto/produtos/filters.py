import django_filters
from .models import Produto, Categoria

class ProdutoFilter(django_filters.FilterSet):
    # Permite filtrar pelo ID da categoria ou pelo nome do acabamento
    categoria = django_filters.ModelChoiceFilter(queryset=Categoria.objects.all())
    acabamento = django_filters.AllValuesFilter() # Permite filtrar por todos os valores de acabamento

    class Meta:
        model = Produto
        fields = ['categoria', 'acabamento']