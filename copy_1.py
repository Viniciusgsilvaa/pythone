class Elevador:
    
    andar = 0
    capacidade = 0

    def __init__(self, andares, capacidade):
        self.__andares = andares
        self.__capacidade = capacidade
    
    def entrar(self, numero):
        if numero + Elevador.capacidade <= self.__capacidade:
            Elevador.capacidade += numero
        else:
            print(f"Exedeu o numero da capacidade do elevador de {self.__capacidade}")
    
    def sair(self, numero):
        if Elevador.capacidade - numero >= 0:
            Elevador.capacidade -= numero
        else:
            print(f"Exedeu o numero de pessoas que estão no elevador")

    def mostra_capacidade(self):
        print(Elevador.capacidade)
    
    def subir(self, andar):
        if Elevador.andar == self.__andares:
            print( "Elevador esta no ultimo andar")
        elif andar + Elevador.andar <= self.__andares:
            Elevador.andar += andar
        else:
            print("Numero excede o valor dos andares")
    
    def descer(self, andar):
        if Elevador.andar == 0:
            print("Elevador esta no terrio")
        elif Elevador.andar - andar >= 0:
            Elevador.andar -= andar
        else:
            print("Exece os andares que tem") 

    def mostra_andar(self):
        print(Elevador.andar)


"""
ele1 = Elevador(10, 6)


ele1.subir(10)
ele1.mostra_andar()
ele1.descer(10)
ele1.mostra_andar()
ele1.descer(1)
"""


class Tv:

    canal = 20
    volume = 0

    def __init__(self, nome, marca, link, volumes, canais):
        self.__nome = nome
        self.__marca = marca
        self.__link = link
        self.__volumes = volumes
        self.__canais = canais
    
    @property
    def link(self):
        return self.__link

    def mostra_som(self):
        print(Tv.volume)
    
    def mostra_canal(self):
        print(Tv.canal)
    
    def aumentar_volume(self):
        if Tv.volume < 100:
            Tv.volume += 1
            print(f' volume : {Tv.volume}')
        else:
            print('Volume no maximo')
    
    def diminuir_volume(self):
        if Tv.volume > 0:
           Tv.volume -= 1
           print(f' volume : {Tv.volume}')
        else:
            print('volume no minimo')

    def aumentar_canal(self):
        if Tv.canal < self.__canais:
            Tv.canal += 1
            print(f'Canal: {Tv.canal}')
        else:
            print('Voce ja esta no ultimo canal')

    def diminuir_canal(self):
        if Tv.canal > 1:
            Tv.canal -= 1
            print(f'Canal: {Tv.canal}')
        else:
            print('Esse e o primeiro canal')

    def escolhercanalc(self, canal):
        if canal <= self.__canais and canal >= 1:
            Tv.canal = canal
            print(f'Canal: {Tv.canal}')
        else:
            print('Numero de canal invalido')


class ControleRemoto:

    def __init__(self, marca, link):
        self.__marca = marca
        self.__link = link
    
    def aumentarocanal(self, link, tv):
        if self.__link == link:
            tv.aumentar_canal()

    def diminuircanal(self, link, tv):
        if self.__link == link:
            tv.diminuir_canal()
    
    def escolhercanal(self, link, canal, tv):
        if self.__link == link:
            tv.escolhercanalc(canal)      


"""
lg = Tv('Lg smart42', 'LG', '1234lg', 100, 20)
lgc = ControleRemoto('LG', '1234lg')
lg.aumentar_volume()
lg.diminuir_volume()
lg.aumentar_canal()
lg.diminuir_canal()
lg.diminuir_canal()
print('-'* 7)

lgc.aumentarocanal(lg.link, lg)
lgc.aumentarocanal(lg.link, lg)
lgc.diminuircanal(lg.link, lg)
lgc.escolhercanal(lg.link, 0, lg)"""


class Moto:
    nmarcha = ['neutro',  'Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta']
    marcha = 2
    
    def __init__(self, marca, modelo, cor, marcha=5):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.ligado = False

    def info(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Marcha: {self.marcha}, Ligada: {self.ligado}')
    
    def infomarcha(self):
        print(Moto.nmarcha[Moto.marcha])


    def passar_marcha(self, marcha):
        Moto.marcha = marcha
        print(Moto.nmarcha[Moto.marcha])

    def marchaacima(self):
        Moto.marcha +=1
    
    def marchaabaixo(self):
        Moto.marcha -= 1

    def Ligar_desligar(self):
        if self.ligado == False:
            self.ligado = True
        else:
            self.ligado = False


"""
honda = Moto('Honda', '150cc', 'verde')
honda.info()
honda.Ligar_desligar()
honda.info()
honda.Ligar_desligar()
honda.info()
honda.passar_marcha(5)
honda.marchaabaixo()
honda.infomarcha()
honda.marchaacima()
honda.infomarcha()"""


class Sobrecarga:
    pass


class Pessoa:

    def __init__(self, codigo, nome, idade):
        self.__codigo = codigo
        self.__nome = nome
        self.__idade = idade

    def exibe(self, x):
        if self.__idade == x:
            print(f' codigo {self.__codigo}, Nome: {self.__nome}, Idade: {self.__idade}')
        else:
            print(f' codigo {self.__codigo}, Nome: {self.__nome}')

    @classmethod
    def construtor_padrao(cls):
        print("Construtor padrão")

b = Pessoa(1, 'Bruno', 34)

b.exibe(34)

