from django.shortcuts import render
from .models import Materia

# Create your views here.

def index(request):
    materia = Materia.objects.all()


    return render(request, 'trabalho/index.html',{
        "materia":materia
    })

