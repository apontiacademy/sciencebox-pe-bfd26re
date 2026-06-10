from django.shortcuts import render, get_object_or_404
from apps.products.models import Produto


def home(request):
    return render(request, 'home.html')


def produto_detalhe(request, id):
    produto = get_object_or_404(Produto, id=id)

    return render(request, 'produto_detalhe.html', {
        'produto': produto
    })


def kits(request):
    produtos = Produto.objects.all()

    return render(request, 'kits.html', {
        'produtos': produtos
    })


def sobre(request):
    return render(request, 'sobre.html')


def solucoes(request):
    return render(request, 'solucoes.html')

def softwares(request):
    return render(request, 'softwares.html')

def contato(request):
    return render(request, 'contato.html')