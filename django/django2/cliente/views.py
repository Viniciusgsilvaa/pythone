from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages


def cliente(request):
    form = ClienteForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Asunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ClienteForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')


    context = {
        'form': form
    } 
    return render(request, 'cliente.html', context)
