from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria,Materia

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome','categoria')
    list_display_links = ('nome',)
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome',)
    


admin.site.register(Categoria)
admin.site.register(Materia, MateriaAdmin)