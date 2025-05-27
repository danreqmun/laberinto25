from hojaObjetos import Totem, Pocima
from objetosMapa import Bolsa
from laberintoBuilder import LaberintoBuilder

class LabBuilderImp(LaberintoBuilder):
    def fabricarTotem(self):
        return Totem()

    def fabricarPocima(self):
        return Pocima()

    def fabricarBolsa(self):
        bolsa = Bolsa()
        bolsa.agregar(Totem())
        bolsa.agregar(Pocima())
        return bolsa