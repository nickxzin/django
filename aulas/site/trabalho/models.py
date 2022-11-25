from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=255)
    subtitulo = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    categoria = models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome