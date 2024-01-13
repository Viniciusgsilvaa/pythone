from django.shortcuts import render
from .models import Produtos
# Create your views here.
def indexprod(request):
    prod = Produtos.objects.all()

    context = {
        'produtos': prod
    }

    return render(request, 'indexprod.html', context)