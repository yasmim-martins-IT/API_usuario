from django.urls import path
from . import views

urlpatterns  = [
    path('criarAdmin/', views.criar_superUser),
    path('criar/', views.criar_User),
    path('logar/', views.logar),
    path('listar/', views.listar_usuarios),
    path('atualizar/<int:pk>', views.atualizar),
    path('deletar/<int:pk>', views.delete),
]