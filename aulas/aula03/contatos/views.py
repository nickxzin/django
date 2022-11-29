from django.http import Http404
from django.db.models import Q, Value
from django.shortcuts import redirect, render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models.functions import Concat
from django.contrib import messages

# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar = True
    )
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
    if not contato.mostrar:
        raise Http404()
    return render(request,'contatos/contatoDetail.html',{
        "contato": contato,
    })

def busca(request):
    busca = request.GET.get("busca")
    if not busca:
        messages.add_message(request, messages.ERROR, 'Campo não pode estar vazio ')
        redirect('index')
    campos = Concat('nome',Value(' '),'sobrenome')
    contatos = Contato.objects.annotate(nomeCompleto = campos).order_by().filter(
        Q(nomeCompleto__icontains = busca)|Q(email__icontains = busca),
        mostrar = True
    )
    paginator = Paginator(contatos,2)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html',{
        "contatos":contatos,
    })