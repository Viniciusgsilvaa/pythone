'''
produto=''
carrinho=[]

while produto != 'sair':
    produto = input('digite um produto ou digite sair para ver o carrinho: ')
    if produto != 'sair':
        carrinho.append(produto)

print(produto)
for produto in carrinho:
    print(produto)

lista = [1, 0, 5, -2, -5, 7]

soma = lista[0]+lista[1]+lista[5]

print(soma)
lista[4]= 100

for n in lista:
    print(n)

    
    a= int(input('Digite quantos valores seram colocados: '))
cont = 0
l=[]
while cont < a:
    r= int(input('Digite um numero:'))
    l.append(r)
    cont+=1
print(l)
receita = {'jan': 100, 'fev': 250, 'mar': 400}


print(receita['jan'])


numeros = [1, 2, 3, 4, 5, 6, 7, 20]

re = [numero * 10 for numero in numeros]

print(re)


amigos = ['maria', 'jose', 'pedro', 'vinicius', 'vanessa']


print([amigo.title() for amigo in amigos])

tripla = lambda x, y: x*3 + y*3

print(tripla(3,3))

A série de Fibonacci é formada pela seqüência 
0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja 
maior que 500.

from random import randint

def lista_numeros(quant, a, b):
    vet = []

    for n in range(20):
        vet.append(randint(a, b))

    return vet

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


    def checa_info(self):
        print(f'{self.__cor}, {self.__voltagem}, {self.__luminosidade}, {self.ligada}')
    
    def ligar_desligar(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def mostra_nome(self):
        return f'{self.__nome} {self.__sobrenome}'

class ContaCorrente:

    contador = 65135416

    def __init__(self, saldo, limite,):
        self.__id = ContaCorrente.contador
        self.__saldo = saldo
        self.__limite = limite
        ContaCorrente.contador += 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    
    def extrato(self):
        print(self.__saldo)
    
    def depositar(self, valor):
        if self.__saldo+valor <= self.__limite:
            self.__saldo += valor
        else:
            print('Deposito invalido, pos exedeu o limete da conta.')
    
    def trasferir(self, valor, conta):
        if self.__saldo >= valor:
            self.__saldo -= valor
            conta.__saldo += valor
        else:
            print('Saldo insuficiente para fazer a trasferencia')


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


c1 = ContaCorrente(300, 2000)
c2 = ContaCorrente(500, 5000)

print(c1.__dict__)
c1.limite = 696969
print(c1.__dict__)
'''


class Animal:

    def __init__(self, nome):
        self.nome = nome
    
    def faz_som(self):
        return f'SOu um animal'

class Aguatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def faz_som(self):
       return f'Sou {self.nome} da agua'

class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def faz_som(self):
        return f'Sou {self.nome} da terra'


class Pinguin(Aguatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aguatico('Willy')
print(baleia.faz_som())
sanchu = Terrestre('Sanshuru')
print(sanchu.faz_som())
tux = Pinguin('Tux')
print(tux.faz_som())