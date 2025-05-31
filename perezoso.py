from modo import Modo
from color import COLOR
import time

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("\nBicho perezoso duerme plácidamente. . .\n")
        time.sleep(2)

    def caminar(self, bicho):
        print("\nBicho perezoso está... andando, o eso parece. . .\n")

    def atacar(self, bicho):
        print("\nBicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace\n")

    def __str__(self):
        return "perezoso"

    def __repr__(self):
        return "perezoso"