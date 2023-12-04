'''
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    
    def informarcao(self):
        print(f'Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}')


class Agenda(Pessoa):

    contador = 1
    agenda = []

    def __init__(self, nome, idade, altura):
        super().__init__(nome, idade, altura)
        self.id = Agenda.contador
        Agenda.contador +=1
        Agenda.agenda.append(object)
    
    def localizacao(self, nome):
        print(nome.id)
    
    def __str__(self):
        return object



p1 = Agenda('Gabriel', 40, 1.80)
p2 = Agenda('Julia', 40, 1.80)
p3 = Agenda('Roberto', 40, 1.80)
p4 = Agenda('Giovana', 40, 1.80)
p5 = Agenda('Barbara', 40, 1.80)
p6 = Agenda('Vinicius', 40, 1.80)


print(Agenda.agenda)

# for n in Agenda.agenda:
#     n.informacao()

'''

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

