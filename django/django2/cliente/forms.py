from django import forms
from django.core.mail.message import EmailMessage
from .models import Cliente

class ClienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nEnail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail= EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudomino.com.br'],
            headers={'reply-to': email}
        )

        mail.send()

class CadastroModelForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'cpf', 'senha']

    senha = forms.CharField(widget=forms.PasswordInput)