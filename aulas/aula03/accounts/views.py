from ast import Return
import email
from http.client import REQUEST_ENTITY_TOO_LARGE
from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email


# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')
def logout(request):
    return render(request, 'accounts/logout.html')
def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    if not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode ficar vazio')
        return render(request, 'accounts/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'EMAIL INVALIDO')
        return render(request, 'accounts/cadastro.html')
    if senha < 3:
        messages.error(request,'SENHA MUITO PEQUENA')
        return render(request, 'accounts/cadastro.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')