""" 23 de febrero """

class ElementoMapa:
    def entrar(self):
        pass

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos = []
        self.padre = None
    
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

class Hoja(ElementoMapa):
    pass

class Decorator(Hoja):
    def __init__(self, elemento):
        self.elemento = elemento
    
    def entrar(self):
        self.elemento.entrar()

class Bomba(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = False

class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

class Pared(ElementoMapa):
    pass

class ParedBomba(Pared):
    def __init__(self):
        self.activa = False

class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2, abierta=False):
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = abierta

class Laberinto:
    def __init__(self):
        self.habitaciones = []
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

class Bicho:
    def __init__(self, vidas, poder, modo):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = None

class Modo:
    pass

class Agresivo(Modo):
    pass

class Perezoso(Modo):
    pass

class Juego:
    def fabricarLaberinto2HabFM(self, unCreator):
        laberinto = Laberinto()
        h1 = Habitacion(1)
        h2 = Habitacion(2)
        puerta = Puerta(h1, h2, abierta=True)
        h1.este = puerta
        h2.oeste = puerta
        laberinto.agregar_habitacion(h1)
        laberinto.agregar_habitacion(h2)
        return laberinto
