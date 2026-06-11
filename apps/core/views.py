from django.shortcuts import render, get_object_or_404
from apps.products.models import Produto
from apps.core.models import Contato


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


def softwares(request):
    return render(request, 'softwares.html')


def contato(request):

    if request.method == 'POST':

        Contato.objects.create(
            nome=request.POST.get('nome'),
            whatsapp=request.POST.get('whatsapp'),
            email=request.POST.get('email'),
            empresa=request.POST.get('empresa'),
            projeto=request.POST.get('projeto')
        )

        return render(request, 'contato.html', {
            'sucesso': True
        })

    return render(request, 'contato.html')