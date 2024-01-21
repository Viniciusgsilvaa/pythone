from django.shortcuts import render
from .forms import ClienteForm, CadastroModelForm
from django.contrib import messages


def cliente(request):
    form = ClienteForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ClienteForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')


    context = {
        'form': form
    } 
    return render(request, 'cliente.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = CadastroModelForm(request.POST or None)
        if form.is_valid():
            form.save()

            messages.success(request, 'Cadastro com Sucesso')
        else:
            messages.error(request, 'Erro ao se cadastrar')
    else:
        form = CadastroModelForm()
    
    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)