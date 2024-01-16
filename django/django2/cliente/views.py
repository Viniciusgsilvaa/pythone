from django.shortcuts import render
from .forms import ClienteForm
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
