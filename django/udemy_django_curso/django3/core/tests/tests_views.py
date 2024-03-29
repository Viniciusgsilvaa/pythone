from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTesteCase(TestCase):

    def setUp(self):
        self.dados = {
        'nome': 'Roberto Carlos',
        'email': 'rbcarlos@gmail.com',
        'assunto': 'Teste assunto',
        'mensagem': 'Testando'
        }
        self.cliente = Client()
    
    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
        'nome': 'Roberto Carlos',
        'email': 'rbcarlos@gmail.com'
        }
        request= self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)