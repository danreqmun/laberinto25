from pared import Pared
from color import COLOR

class ParedFlecha(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, alguien):
        if self.activa:
            print(f"{COLOR.ALGOMALO} te has chocado contra una pared flecha {COLOR.FIN}")
            alguien.vidas = alguien.vidas - 1
            print(f"{alguien} ha perdido 1 pto de vida. Vidas restantes: {alguien.vidas}")
            if alguien.vidas <= 0:
                alguien.vidas = 0
                alguien.estadoEnte.morir(alguien)
            self.activa = False
        else:
            print(f"La pared flecha ya ha hecho daño o está desactivada")