from django.shortcuts import render
from core.models import Produto
# Create your views here.


def index(request):
    # print(dir(request.user))
    # print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário logado'
    
    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação web com Django Framework',
        'outro': 'Django é massa!',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    item = Produto.objects.get(id=id)
    context = {
        'produto': item
    }
    return render(request, 'produto.html', context)