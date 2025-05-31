from pared import Pared
from color import COLOR

class ParedFlecha(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, alguien):
        if self.activa:
            print(f"{COLOR.ALGOMALO} {alguien} ha chocado contra una pared flecha {COLOR.FIN}")
            alguien.vidas = alguien.vidas - 1
            if alguien.vidas <= 0:
                alguien.vidas = 0
                alguien.estadoEnte.morir(alguien)
            print(f"{COLOR.ORADOR} {alguien} ha perdido 1 pto de vida. Vidas restantes: {alguien.vidas} {COLOR.FIN}")
            self.activa = False
        else:
            print(f"{COLOR.ORADOR}La pared flecha ya ha hecho daño o está desactivada {COLOR.FIN}")