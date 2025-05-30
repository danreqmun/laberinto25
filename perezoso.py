from modo import Modo
from color import COLOR
import time

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Bicho perezoso duerme plácidamente. . . . .")
        time.sleep(2)

    def caminar(self, bicho):
        print("Bicho perezoso está... andando, o eso parece. . .")

    def atacar(self, bicho):
        print("Bicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace")

    def __str__(self):
        return "perezoso"

    def __repr__(self):
        return "perezoso"