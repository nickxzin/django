from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'contatos/index.html')

def contatos(request):
    contatos = Contato.objects.order_by('nome').filter(mostrar = True)
    paginator = Paginator(contatos, 1)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/contatos.html',{
        'contatos': contatos
    })
def verContato(request,contatoNome):
    # contato= Contato.objects.get(nome=contatoNome)
    contato = get_object_or_404(Contato,nome=contatoNome)
    if not contato.mostrar:
        raise Http404()
    return render(request, 'contatos/verContato.html',{
        'contato': contato
    })
def busca(request):
    busca = request.GET.get('busca')
    if not busca : #linha nova
        messages.add_message(request, messages.ERROR,'Campo não pode ficar vazio')
        return redirect('contatos')
    campos = Concat('nome',Value(' '),'sobrenome') #linha nova
    contatos = Contato.objects.annotate( #linha nova
        nomeCompleto = campos #linha nova
    ).order_by('nome').filter( #linha nova 
        Q(nomeCompleto__icontains = busca)|Q(telefone__icontains = busca), #linha nova
        mostrar = True#linha nova
    ) #linha nova
    paginator = Paginator(contatos, 1)
    page = request.GET.get('page')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html',{
        'contatos': contatos
    })