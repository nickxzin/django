from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contatos/', views.contatos, name='contatos'),
    path('busca/', views.busca, name='busca'),
    path('<str:contatoNome>', views.verContato, name='verContato'),
]