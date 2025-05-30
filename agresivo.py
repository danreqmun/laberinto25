import time
from modo import Modo
from color import COLOR

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Bicho agresivo está durmiendo. . .")
        time.sleep(1)

    def caminar(self, bicho):
        print("Bicho agresivo está caminando. . . agresivamente. . .")
        bicho.caminar()

    def atacar(self, bicho):
        print("Bicho agresivo ha atacado con furia titánica")
        bicho.atacar()

    def __str__(self):
        return "agresivo"