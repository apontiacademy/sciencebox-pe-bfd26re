from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.produto_detalhe, name='produto_detalhe'),
]