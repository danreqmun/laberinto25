# FACTORY METHOD --- COMPONENT
class ElementoMapa:
    def __init__(self):
        self.padre = None

    def recorrer(self, func):
        func(self)

    def entrar(self, alguien):
        pass

    def esPuerta(self):
        return False

    def aceptar(self, unVisitor):
        pass

    def calcularPosicionDesde(self,forma):
        pass

    def calcularPosicion(self):
        pass

    def calcularPosicionDesdeEn(self,forma, punto):
        pass