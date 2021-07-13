from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto, Avaliacao


def index(request):
    produtos = Produto.objects.all()
    avaliacao = Avaliacao.objects.all()

    context = {
        'curso': 'Programação Web com Django',
        'outro': 'Django é massa!',
        'produtos': produtos,
        'avaliacao': avaliacao,
    }
    return render(request, 'index.html', context)





'''
def avaliacao(request, pk):
    aval = Avaliacao.objects.get(id=pk)

    context = {
        'avaliacao': aval

    }

    return render(request, 'avaliacao.html', context)
'''


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)


