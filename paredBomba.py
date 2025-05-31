from pared import Pared
from color import COLOR

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, ente):
        if self.activa:
            print(f"{COLOR.ALGOMALO} {ente} ha chocado contra una pared bomba {COLOR.FIN}")
            ente.vidas = ente.vidas - 2
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            print(f"{COLOR.ORADOR} {ente} ha perdido 2 ptos de vida. Vidas restantes: {ente.vidas} {COLOR.FIN}")

            self.activa = False
        else:
            print(f"{COLOR.ORADOR}La pared bomba ya ha explotado o está desactivada {COLOR.FIN}")

    """def esActiva(self):
        if self.activa:
            return COLOR.MONOLOGO + "Hmm, parece una pared normal y corriente... espero que no... explote..." + COLOR.FIN
        else:
            return COLOR.MONOLOGO + "Creo que es una pared... normal... como las demás..." + COLOR.FIN

    def activar_pared_bomba(self):
        self.activa = True

    def desactivar_pared_bomba(self):
        self.activa = False"""

    def __repr__(self):
        return "Pared bomba"