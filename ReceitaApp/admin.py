from django.contrib import admin
from ReceitaApp.models import Categoria, Receita

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    list_display_links = ['id', 'nome']
    search_fields = ['nome']
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ingredientes', 'preparo', 'dificuldade']
    


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Receita, ReceitaAdmin)