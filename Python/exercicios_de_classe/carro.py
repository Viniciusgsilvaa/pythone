class Carro:

    marcha = 0
    velocidade = 0
    lugares = 0


    def __init__(self, marca, marcha, velocidade , lugares):
        self.__marca = marca
        self.__marcha = marcha
        self.__velocidade = velocidade
        self.__lugares = lugares
        self.__ligado = False
    
    def info(self):
        return f'Marca = {self.__marca}, Limete de Marcha = {self.__marcha}, Limite de velocidade = {self.__velocidade}KM/h, Limite de Lugares = {self.__lugares}'
    
    def aumentar_marcha(self):
        if Carro.marcha < self.__marcha:
            Carro.marcha += 1 
            Carro.velocidade += self.__velocidade // self.__marcha
        else:
            print('ultima marcha')
    
    def diminuir_marcha(self):
        if Carro.marcha > 0:
            Carro.marcha -= 1
            Carro.velocidade -= self.__velocidade // self.__marcha
        else:
            print('Ponto Neutro')
    

    def mostrar_marcha_velocidade(self):
        nmarcha = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta']
        print(f'Marcha: {nmarcha[Carro.marcha]}, Velocidade: {Carro.velocidade}')
    
    def bozinar():
        print('Biiiiiiibiiiii')
    
    def entrar_no_carro(self, lugar=1):
        if Carro.lugares + lugar <= self.__lugares:
            Carro.lugares += lugar
            
        else:
            print('Excedeu o limite de acentos')
    
    def sair_do_carro(self, lugar=1):
        if Carro.lugares - lugar >= 0:
            Carro.lugares -= lugar
            

    def mostrar_lugares(self):
        print(f'A {self.__lugares} lugares nesse carro, e {self.__lugares - Carro.lugares} Vagos')


    
carro1 = Carro('Honda', 5, 150, 4)

