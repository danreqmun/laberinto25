from modo import Modo
from color import COLOR
import time

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso duerme plácidamente. . . . ." + COLOR.FIN)
        time.sleep(2)

    def caminar(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso está... andando, o eso parece. . ." + COLOR.FIN)

    def atacar(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace" + COLOR.FIN)

    def __str__(self):
        return "perezoso"

    def __repr__(self):
        return "perezoso"