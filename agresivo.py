import time
from modo import Modo
from color import COLOR

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("\nBicho agresivo está durmiendo. . .\n")
        time.sleep(1)

    def caminar(self, bicho):
        print("\nBicho agresivo está caminando. . . agresivamente. . .\n")
        bicho.caminar()

    def atacar(self, bicho):
        print("\nBicho agresivo ha atacado con furia titánica\n")
        bicho.atacar()

    def __str__(self):
        return "agresivo"