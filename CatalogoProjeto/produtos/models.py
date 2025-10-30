# produtos/models.py
from django.db import models
from django.conf import settings 
from urllib.parse import quote # Importado para codificar a URL

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # CORREÇÃO DO ERRO '...' e adição de flexibilidade para evitar OperationalError
    link_foto_principal = models.URLField(
        verbose_name='Foto Principal do Produto',
        max_length=500,
        blank=True,
        null=True
    )
    
    link_foto_ambiente = models.URLField(
        verbose_name='Foto de Aplicação/Ambiente', 
        max_length=500,
        blank=True, 
        null=True
    )
    
    # Adicionando blank=True para que não sejam obrigatórios e não causem erro de migração
    detalhes = models.TextField(blank=True)
    acabamento = models.CharField(max_length=50, blank=True) # Ex: Polido, Acetinado

    def get_whatsapp_link(self):
        # Acessa o número definido no settings.py (ou use o número fixo)
        base_num = getattr(settings, 'WHATSAPP_NUMBER', "5511999999999") 
        mensagem = (
            f"Olá! Gostaria de um orçamento para o item:\n"
            f"Nome: {self.nome}\n"
            f"Código: {self.codigo}\n"
        )
        return f"https://wa.me/{base_num}?text={quote(mensagem)}"

    def __str__(self):
        return self.nome