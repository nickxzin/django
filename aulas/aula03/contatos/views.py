from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'contatos/index.html')

def sobre(request):
    return render(request, 'contatos/sobre.html')