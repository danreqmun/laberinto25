from color import COLOR
from decorator import Decorator

class Flecha(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = True

    def entrar(self, ente):
        # Primero se ejecuta la lógica original del elemento decorado
        self.elemento.entrar(ente)

        # Ahora la lógica del cohete
        if self.activa:
            print(f"{COLOR.ALGOMALO} {ente} le ha dado un flecha (decorator) {COLOR.FIN}")
            ente.vidas -= 1
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            print(f"{COLOR.ORADOR} {ente} pierde una vida. Vidas restantes: {ente.vidas} {COLOR.FIN}")
            self.activa = False
        else:
            print(f"{COLOR.ORADOR}La flecha del decorador ya se usó{COLOR.FIN}")


    def esFlecha(self):
        return True

    def __repr__(self):
        return "Flecha"