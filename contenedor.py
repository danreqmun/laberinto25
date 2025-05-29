from elementoMapa import ElementoMapa


# COMPOSITE
class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []
        self.forma = None


    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminarHijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.forma.agregarOrientacion(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.forma.eliminarOrientacion(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        self.forma.ponerElementoEnOrientacion(elemento, orientacion)

    def obtenerElementoEnOrientacion(self, orientacion):
        return self.forma.obtenerElementoEnOrientacion(orientacion)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)

    def caminarAleatorio(self, bicho):
        self.forma.caminarAleatorio(bicho)

    def aceptar(self, unVisitor):
        self.visitarContenedor(unVisitor)
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)
        self.forma.aceptar(unVisitor)