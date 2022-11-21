from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos,2)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
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