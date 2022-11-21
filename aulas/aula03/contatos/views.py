from django.shortcuts import render, get_object_or_404
from .models import Contato

# Create your views here.

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',{
        "contatos":contatos
    })

def sobre(request):
    return render(request, 'contatos/sobre.html')

def contatoDetail(request,nomeContato):
    contato = get_object_or_404(Contato,nome=nomeContato)
    return render(request,'contatos/contatoDetail.html',{
        "contato": contato
    })