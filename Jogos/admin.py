from django.contrib import admin
from .models import Genero, Jogo , Plataforma , Desenvolvedor

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 4

class ListandoGenero(admin.ModelAdmin):
    list_display = ('id','tipo')
    list_display_links = ('id', 'tipo')
    search_fields = ('tipo',)
    list_per_page = 4

class ListandoJogo(admin.ModelAdmin):
    list_display = ('id', 'nome', 'publicar')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_editable = ('publicar',)
    list_per_page = 4

class ListandoPlataforma(admin.ModelAdmin):
    list_display = ('id','nomePla')
    list_display_links = ('id', 'nomePla')
    search_fields = ('nomePla',)
    list_per_page = 4

class ListandoDesenvolvedor(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 4

admin.site.register(Genero, ListandoGenero)
admin.site.register(Jogo, ListandoJogo)
admin.site.register(Plataforma, ListandoPlataforma)
admin.site.register(Desenvolvedor, ListandoDesenvolvedor)