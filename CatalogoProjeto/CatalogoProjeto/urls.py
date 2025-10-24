# CatalogoProjeto/urls.py
from django.contrib import admin
from django.urls import path, include # Adicione 'include'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Conecta as URLs do catálogo à raiz do site
    path('', include('produtos.urls')), 
]