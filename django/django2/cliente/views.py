from django.shortcuts import render

def cliente(request):
    return render(request, 'cliente.html')
