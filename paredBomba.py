from pared import Pared
from color import COLOR

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, ente):
        if self.activa:
            print(f"{COLOR.ALGOMALO} te has chocado contra una pared bomba {COLOR.FIN}")
            ente.vidas = ente.vidas - 1
            print(f"{ente} ha perdido 1 pto de vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.activa = False
        else:
            print("La pared bomba ya ha explotado o está desactivada")

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