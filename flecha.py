from color import COLOR
from decorator import Decorator

class Flecha(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = False

    def entrar(self, alguien):
        if not self.activa:
            print(f"{COLOR.ALGOMALO} Flecha activada... ¡zas! {COLOR.FIN}")
            alguien.vidas -= 1
            print(f"{alguien} pierde 1 pto de vida. Vidas restantes: {alguien.vidas}")
            self.activa = True
        else:
            print("Flecha ya usada")

        # Pasar al comportamiento base
        self.elemento.entrar(alguien)

    def esFlecha(self):
        return True

    def __repr__(self):
        return "Flecha"