from django.contrib import admin
from .models import Categoria,Contato

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','categoria','mostrar')
    list_display_links = ('nome', 'sobrenome',)
    list_filter = ('categoria',)
    list_per_page = 10
    search_fields = ('nome',"sobrenome")
    list_editable = ('mostrar',)



admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)