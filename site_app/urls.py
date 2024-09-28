from django.urls import path
from site_app import views

urlpatterns = [
    path('', views.home),
    path('cadastro_colaborador/', views.cadastro_colaborador, name='cadastro_colaborador'),
    path('lista_colaborador/', views.lista_colaborador, name='lista_colaborador'),
    path('deletar_colaborador/<int:id>/', views.deletar_colaborador, name='deletar_colaborador'),
    path('atualizar_colaborador/<int:id>/', views.atualizar_colaborador, name='atualizar_colaborador'),
]
