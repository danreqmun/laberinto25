from decorator import Decorator


class Bomba(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = False

    """def activar_bomba(self):
        self.activa = True"""

    def aceptar(self, unVisitor):
        unVisitor.visitarBomba(self)

    def esBomba(self):
        return True

    def __repr__(self):
        return "Bomba"