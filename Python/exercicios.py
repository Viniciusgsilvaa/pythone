# Exercicios de POO
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def informarcao(self):
        print(f'Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}')


class Agenda:
    def __init__(self):
        self.pessoas = []

    def armazenar_pessoa(self, nome, idade, altura):
        pessoa = {'nome': nome, 'idade': idade, 'altura': altura}
        if len(self.pessoas) < 10:
            self.pessoas.append(pessoa)
            print(f'{nome} foi armazenado na posição {len(self.pessoas)} da agenda.')
        else:
            print('A agenda está cheia. Não é possível adicionar mais pessoas.')

    def busca_pessoa(self, nome):
        for i, pessoa in enumerate(self.pessoas, start=1):
            if pessoa['nome'] == nome:
                return i
        return -1

    def imprime_agenda(self):
        for i, pessoa in enumerate(self.pessoas, start=1):
            print(f'Posição {i}: {pessoa["nome"]}, {pessoa["idade"]} anos, {pessoa["altura"]} cm')

    def imprime_pessoa(self, index):
        if 1 <= index <= len(self.pessoas):
            pessoa = self.pessoas[index - 1]
            print(f'Posição {index}: {pessoa["nome"]}, {pessoa["idade"]} anos, {pessoa["altura"]} cm')
        else:
            print('Posição inválida. Forneça um índice válido.')

# Exemplo de uso:
agenda = Agenda()

agenda.armazenar_pessoa("João", 30, 175)
agenda.armazenar_pessoa("Maria", 25, 160)

posicao_maria = agenda.busca_pessoa("Maria")
print(f'A pessoa Maria está na posição {posicao_maria} da agenda.')

agenda.imprime_agenda()
agenda.imprime_pessoa(1)


# EXERCICIOS DE LIST COMPREHENSION

"""Crie uma lista dos quadrados dos números ímpares de 1 a 10.

Dada uma lista de palavras, crie uma nova lista contendo o comprimento de cada palavra.

Dada uma lista de números, crie uma nova lista contendo apenas os números pares elevados ao quadrado.

Crie uma lista de todas as letras da palavra "compreensao" que não são vogais.

Dada uma lista de strings, crie uma nova lista contendo apenas as strings que têm mais de três caracteres.

Crie uma matriz 3x3 e, em seguida, crie uma lista com os elementos dessa matriz."""


impares = [x for x in range(1, 11) if x % 2 != 0]
print(impares)

listadepalavras = ['Ola', 'sou', 'um', 'teste', 'como', 'paralelepipedo', 'incostitucionalicimamente' ]

lc = [len(palavras) for palavras in listadepalavras]
print(lc)

parele = [x**2 for x in range(1, 20) if x %2 == 0]
print(parele)

cons = [x for x in 'compreensao' if x in 'cmprns']
print(cons)

listadestring = ['Ola', 'sou', 'um', 'teste', 'como', 'paralelepipedo', 'incostitucionalicimamente' ]

nl = [x for x in listadestring if len(x) > 3]
print(nl)

matrix = [[x for x in range(1,4)] for x in range(1,4)]
print(matrix)

"""
Crie uma lista dos quadrados dos números pares de 0 a 9 usando compreensão de lista.

Crie uma lista dos múltiplos de três de 1 a 20 usando compreensão de lista.

Dada uma lista original, crie uma nova lista que seja uma cópia da original, mas com todos os números pares multiplicados por 2.

Dada uma string, crie uma lista contendo apenas as letras maiúsculas da string.

Crie uma lista dos números primos de 1 a 50 usando compreensão de lista.

Dada uma matriz quadrada matriz, crie uma nova matriz que seja a transposta da matriz original usando compreensão de lista.

Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que têm menos de 5 caracteres.

Dadas duas listas a e b, crie uma lista contendo todos os pares (x, y) onde x é de a e y é de b.

Dada uma string, crie uma lista contendo apenas os caracteres únicos na string, preservando a ordem original.

Dada uma lista de números, crie uma nova lista contendo os números negativos.
"""

quad = [x**2 for x in range(10) if x % 2 == 0]
print(quad)

muttre = [x for x in range(1, 21) if x % 3 == 0]
print(muttre)

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cop = [x*2 if x % 2 == 0 else x for x in lis]
print(cop)

a = 'UHoçjHOUHohHoiFGikHFu8viYF'
uper = [letra for letra in a if letra.isupper()]
print(uper)

primos = [x for x in range(1, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primos)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = [[linha[i] for linha in matriz] for i in range(len(matriz))]
print(transposta)

liststring = ['Ola', 'sou', 'um', 'teste', 'como', 'paralelepipedo', 'incostitucionalicimamente' ]
novalis = [palavra for palavra in liststring if len(palavra) < 5]
print(novalis)

a = [1, 2, 3]
b = ['a', 'b', 'c']
pares = [(x, y) for x in a for y in b ]
print(pares)

string = "lnçaoddh.jrgRHNGSIOBNRG.NAÇPRKGJPAKRENGPKu"
unicos = [unico for unico in string if string.count(unico) == 1]
print(unicos)

numeros = [-2, 0, 5, -8, 10, -3]
negativa = [x for x in numeros if x < 0]
print(negativa)

"""
Números Ímpares ao Cubo:
Crie uma lista dos cubos dos números ímpares de 1 a 10 usando compreensão de lista.

Números Divisíveis por 3 e 5:
Crie uma lista dos números de 1 a 30 que são divisíveis por 3 e 5 ao mesmo tempo.

Invertendo Palavras:
Dada uma lista de palavras, crie uma nova lista contendo cada palavra invertida.

Múltiplos de 2 ou 3:
Crie uma lista dos números de 1 a 20 que são múltiplos de 2 ou 3.

Contagem de Vogais:
Dada uma string, crie uma lista contendo tuplas onde o primeiro elemento é uma vogal e o segundo elemento é a contagem dessa vogal na string.

Compreensão de Lista com Condições Aninhadas:
Crie uma compreensão de lista que gere uma lista dos quadrados dos números ímpares no intervalo de 1 a 20, mas apenas para os números que não são divisíveis por 3.
"""

impa = [x**3 for x in range(1, 10) if x %2 != 0]
print(impa)

multcin = [x for x in (1, 30) if x % 3 == 0 and x % 5 == 0]
print(multcin)

palavras = ["python", "java", "c", "javascript", "html"]
revp = [palavra[::-1] for palavra in palavras]
print(revp)

muit = [x for x in range(1, 21) if x %2 == 0 or x %3 == 0]
print(muit)

string = "exemplo de string"
contvog = [(x, string.count(x)) for x in string]
print(contvog)

des = [x**2 for x in range(1, 21) if x %2 != 0 and x%3 == 0]
