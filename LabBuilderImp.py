from Juego import *
from LabBuilder import *

class LabBuilderImp(LabBuilder):
    def fabricarTotem(self):
        return Totem()

    def fabricarPocima(self):
        return Pocima()

    def fabricarBolsa(self):
        bolsa = Bolsa()
        bolsa.agregar(Totem())
        bolsa.agregar(Pocima())
        return bolsa