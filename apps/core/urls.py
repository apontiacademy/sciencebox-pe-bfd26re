from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('kits/', views.kits, name='kits'),
    path('sobre/', views.sobre, name='sobre'),
    path('softwares/', views.softwares, name='softwares'),
    path('contato/', views.contato, name='contato'),

    path(
        'software-detalhe/',
        views.software_detalhe,
        name='software_detalhe'
    ),

    path(
        'produto/<int:id>/',
        views.produto_detalhe,
        name='produto_detalhe'
    ),
]