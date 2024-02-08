from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(username=username).first():
            return HttpResponse('Ja existe um usuario com esse nome ')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Sua conta foi criada com sucesso')

def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
    
    user = authenticate(username=username, password=senha)

    if user:
        login(request, user)
        return HttpResponse('Bem vindo usuario')
    else:
        return HttpResponse('Login ou senha invalido')
    
@login_required(login_url='/auth/login/')
def plataforma(request):
    return HttpResponse('Precisa estar logado')