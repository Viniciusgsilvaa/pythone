class Carro:

    def __init__(self, marca, marcha, velocidade , lugares):
        self.__marca = marca
        self.__marcha = marcha
        self.__velocidade = velocidade
        self.__lugares = lugares
    
    def info(self):
        return f'Marca = {self.__marca}, Limete de Marcha = {self.__marcha}, Limite de velocidade = {self.__velocidade}KM/h, Limite de Lugares = {self.__lugares}'
    
carro1 = Carro('Honda', 5, 150, 4)
print(carro1.info())