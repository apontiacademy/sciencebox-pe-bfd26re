from django.shortcuts import render, get_object_or_404
from .models import Produto


def produto_detalhe(request, id):
    produto = get_object_or_404(
        Produto,
        id=id
    )

    return render(
        request,
        'produto_detalhe.html',
        {'produto': produto}
    )