from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request,'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request,username=usuario,password=senha)
    if not user:
        messages.error(request, 'Usuario ou senha incorreto')
        return render(request,'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request,'Você Logou!')
        return redirect('dashboard')
def logout(request):
    auth.logout(request)
    messages.success(request,'Você Deslogou!')
    return redirect('login')
def cadastro(request):
    if request.method != 'POST':
        return render(request,'accounts/cadastro.html')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2  = request.POST.get('senha2')
    if not email or not usuario or not senha or not senha2:
        messages.error(request,'OS CAMPOS NAO PODEM ESTAR VAZIOS')
        return render(request,'accounts/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.error(request,'EMAIL INVALIDO')
        return render(request,'accounts/cadastro.html')
    if User.objects.filter(username=usuario).exists():
        messages.error(request,'USUARIO JA EXISTE')
        return render(request,'accounts/cadastro.html')
    if User.objects.filter(email=email).exists():
        messages.error(request,'EMAIL JA EXISTE')
        return render(request,'accounts/cadastro.html')
    messages.success(request,'Registrado com sucesso')
    user = User.objects.create_user(username=usuario, email=email,
    password=senha)
    user.save()
    return redirect('login')
@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')