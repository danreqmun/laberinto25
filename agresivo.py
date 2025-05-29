import time
from modo import Modo
from color import COLOR

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo está durmiendo. . ." + COLOR.FIN)
        time.sleep(1)

    def caminar(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo está caminando. . . agresivamente. . ." + COLOR.FIN)
        bicho.caminar()

    def atacar(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo ha atacado con furia titánica" + COLOR.FIN)
        bicho.atacar()

    def __str__(self):
        return "agresivo"