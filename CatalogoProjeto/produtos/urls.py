# produtos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo_lista'),
    path('sobre/', views.sobre_a_marca, name='sobre_a_marca'),
]