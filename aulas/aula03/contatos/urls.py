from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('<str:nomeContato>',views.contatoDetail,name='contatoDetail'),
    path('busca/',views.busca,name='busca'),
]