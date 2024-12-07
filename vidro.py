from residuo import Residuo

class Vidro(Residuo):
    def __init__(self, massa, tipo, reciclavel):
        super().__init__(massa, tipo)
        self.__reciclavel = True
        self._tipo = "Vidro"

    def getReciclavel(self):
        return self.__reciclavel
    def setReciclavel(self, reciclavel):
        self.__reciclavel = reciclavel

    def mostrar(self):
        return (f"Tipo: {self.getTipo()}; Massa: {self.getMassa()}Kg; Resíduo reciclável.")