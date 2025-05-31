from totem import Totem
from pocima import Pocima
import bolsa as Bolsa
from laberintoBuilder import LaberintoBuilder

class LabBuilderImp(LaberintoBuilder):
    def fabricarTotem(self):
        return Totem()

    def fabricarPocima(self):
        return Pocima()

    def fabricarBolsa(self):
        bolsa = Bolsa.Bolsa()
        bolsa.agregar(self.fabricarPocima())
        bolsa.agregar(self.fabricarPocima())
        return bolsa