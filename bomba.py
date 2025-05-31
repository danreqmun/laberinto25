from decorator import Decorator
from color import COLOR

class Bomba(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = True

    """def activar_bomba(self):
        self.activa = True"""

    def entrar(self, ente):
        # Primero se ejecuta la lógica original del elemento decorado
        self.elemento.entrar(ente)

        # Ahora la lógica del cohete
        if self.activa:
            print(f"{COLOR.ALGOMALO} {ente} le ha dado una bomba (decorator) {COLOR.FIN}")
            ente.vidas -= 1
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            print(f"{COLOR.ORADOR} {ente} pierde una vida. Vidas restantes: {ente.vidas} {COLOR.FIN}")
            self.activa = False
        else:
            print(f"{COLOR.ORADOR}El cohete del decorador ya se usó{COLOR.FIN}")

    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)

    def esBomba(self):
        return True

    def __repr__(self):
        return "Bomba"