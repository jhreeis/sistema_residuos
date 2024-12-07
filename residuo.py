from abc import ABC, abstractmethod
class Residuo(ABC):
    def __init__(self, massa, tipo):
        self.__massa = massa
        self.__tipo = tipo
 
    def getMassa(self):
        return self.__massa
    def getTipo(self):
        return self.__tipo
    
    def setMassa(self, massa):
        self.__massa = massa
    def setTipo(self, tipo):
        self.__tipo = tipo

    @abstractmethod
    def mostrar(self):
        pass