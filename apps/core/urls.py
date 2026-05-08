from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('kits/', views.kits, name='kits'),
    path('sobre/', views.sobre, name='sobre'),
    path('solucoes/', views.solucoes, name='solucoes'),
    path('contato/', views.contato, name='contato'),

    path(
        'produto/<int:id>/',
        views.produto_detalhe,
        name='produto_detalhe'
    ),
]