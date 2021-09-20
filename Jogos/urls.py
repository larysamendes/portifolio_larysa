from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:jogo_id>' , jogo, name='jogo'),
    path('buscar', buscar, name='buscar'),
    path('cria/jogos', cria_jogo, name='cria_jogo' ),
    path('deleta/<int:jogo_id>', deleta_jogo, name= 'deleta_jogo'),
    path('edita/<int:jogo_id>', edita_jogo, name= 'edita_jogo'),
    path('atualiza_jogo', atualiza_jogo, name='atualiza_jogo'),
    path('cria/genero', cria_genero, name='cria_genero' ),
    path('cria/plataforma', cria_plataforma, name='cria_plataforma' ),
    path('cria/desenvolvedor', cria_desenvolvedor, name='cria_desenvolvedor' ),


]