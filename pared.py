from elementoMapa import ElementoMapa
from color import COLOR

class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self, alguien):
        print(COLOR.ALGOMALO + "te has chocado contra una pared" + COLOR.FIN)

    def __repr__(self):
        return "Pared"