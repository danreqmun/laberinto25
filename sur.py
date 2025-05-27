from orientacion import Orientacion
from point import Point

class Sur(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.sur = elemento

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

    def obtenerElemento(self, forma):
        return forma.sur

    def caminarAleatorio(self, ente, forma):
        forma.sur.entrar(ente)

    def aceptar(self, unVisitor, forma):
        forma.sur.aceptar(unVisitor)

    def calcularPosicionDesde(self, forma):
        unPunto = Point(forma.punto.x,forma.punto.y+1)
        forma.sur.calcularPosicionDesdeEn(forma,unPunto)

    def __repr__(self):
        return "sur"