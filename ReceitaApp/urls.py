from django.urls import path
from ReceitaApp import views

urlpatterns = [
        #(caminho,    View Correpondente,   nome da URL)
    path('', views.index, name='index'),
    path('receitas/', views.listar_receitas, name='receitas'),
]

#Para cada URl do site, coloco uma linha nessa lista URLpatterns
