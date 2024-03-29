from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTesteCase(TestCase):
    
    def setUp(self):
        self.nome = 'Roberto Carlos'
        self.email = 'rbcarlos@gmail.com'
        self.assunto = 'Teste assunto'
        self.mensagem = 'Testando'
    
        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)