from orientacion import Orientacion
from point import Point

class Este(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.este = elemento

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

    def obtenerElemento(self, forma):
        return forma.este

    def caminarAleatorio(self, ente, forma):
        forma.este.entrar(ente)

    def aceptar(self, unVisitor, forma):
        forma.este.aceptar(unVisitor)

    def calcularPosicionDesde(self, forma):
        unPunto = Point(forma.punto.x+1,forma.punto.y)
        forma.este.calcularPosicionDesdeEn(forma,unPunto)

    def __repr__(self):
        return "este"