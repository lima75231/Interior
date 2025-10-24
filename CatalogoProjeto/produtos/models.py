from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) # Para URLs limpas

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    link_foto = models.URLField(verbose_name='Link da Foto Principal', 
        max_length=500)
    detalhes = models.TextField()
    acabamento = models.CharField(max_length=50) # Ex: Polido, Acetinado

    def get_whatsapp_link(self):
        base_num = "5511999999999" # SEU NÚMERO
        msg = f"Olá! Gostaria de um orçamento para o item: {self.nome} (Cód: {self.codigo})."
        # O Python fará a codificação do texto
        return f"https://api.whatsapp.com/send?phone={base_num}&text={msg.replace(' ', '%20')}"

    def __str__(self):
        return self.nome

# Aplica as mudanças no banco de dados (Cria as tabelas)
# (venv) python manage.py makemigrations
# (venv) python manage.py migrate