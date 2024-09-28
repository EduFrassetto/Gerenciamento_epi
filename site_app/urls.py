from django.urls import path
from site_app import views

urlpatterns = [
    path('', views.home),
    path('cadastro_colaborador/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('lista_colaborador/', views.lista_colaborador, name='lista_colaborador'),
    path('deletar_colaborador/<int:id>/', views.deletar_colaborador, name='deletar_colaborador'),
    path('atualizar_colaborador/<int:id>/', views.atualizar_colaborador, name='atualizar_colaborador'),
    path('cadastro_epi/', views.cadastro_epi, name='cadastro_epi'),
    path('lista_epi/', views.lista_epi, name='lista_epi'),
    path('deletar_epi/<int:id>/', views.deletar_epi, name='deletar_epi'),
    path('atualizar_epi/<int:id>/', views.atualizar_epi, name='atualizar_epi'),
]
