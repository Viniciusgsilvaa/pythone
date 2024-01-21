from django.db import models


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    cpf = models.CharField('Cpf', max_length=14)
    senha = models.CharField('Senha', max_length=20)

    def __str__(self):
        return self.nome

