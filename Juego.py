""" 19/05/25 """

import copy
import json
import threading
import time
import random
#from point import Point
import tkinter as tk

class COLOR:
    FIN = '\033[0m'   # hay que ponerlo al final de cada frase o si no el resto del programa usará el color anterior
    ORADOR = '\033[93m' # orador
    ALGOMALO = '\033[91m'     # algo malo
    MONOLOGO = '\033[94m'     # monologo
    PARPADEO = '\033[5m'      # el texto parpadea
    WARNINGACCION = '\033[41m'



# FACTORY METHOD --- COMPONENT
class ElementoMapa:
    def __init__(self):
        self.padre = None

    def recorrer(self, func):
        func(self)

    def entrar(self):
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

class Visitor:
    def visitarHabitacion(self, habitacion):
        pass

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        pass

    def visitarBomba(self, bomba):
        pass

    def visitarTunel(self, tunel):
        pass


class Forma:
    def __init__(self):
        self.orientaciones = []
        self.num = None
        self.punto = Point(0,0)
        self.extent = Point(0, 0)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)

    def recorrer(self, func):
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)

    def calcularPosicion(self):
        for orientacion in self.orientaciones:
            orientacion.calcularPosicionDesde(self)

    def caminarAleatorio(self, ente):
        orientacion=self.obtenerOrientacionAleatoria()
        print(f"Orientacion aleatoria: {orientacion}")
        orientacion.caminarAleatorio(ente, self)

    def obtenerOrientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def aceptar(self, unVisitor):
        for orientacion in self.orientaciones:
            orientacion.aceptar(unVisitor, self)


class Cuadrado(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.orientaciones = []


# LEAF
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()



# SINGLETON
class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        pass

    def recorrer(self, func, forma):
        pass

    def obtenerElemento(self, forma):
        pass

    def caminarAleatorio(self, bicho, forma):
        pass

    def aceptar(self, unVisitor, forma):
        pass

    def calcularPosicionDesde(self, forma):
        pass

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte = elemento

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def obtenerElemento(self, forma):
        return forma.norte

    def caminarAleatorio(self, ente, forma):
        forma.norte.entrar(ente)

    def aceptar(self, unVisitor, forma):
        forma.norte.aceptar(unVisitor)

    def calcularPosicionDesde(self, forma):
        unPunto = Point(forma.punto.x,forma.punto.y-1)
        forma.norte.calcularPosicionDesdeEn(forma,unPunto)

    def __repr__(self):
        return "norte"

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

class Oeste(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.oeste = elemento

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)

    def obtenerElemento(self, forma):
        return forma.oeste

    def caminarAleatorio(self, ente, forma):
        forma.oeste.entrar(ente)

    def aceptar(self, unVisitor, forma):
        forma.oeste.aceptar(unVisitor)
    def calcularPosicionDesde(self, forma):
        unPunto = Point(forma.punto.x-1,forma.punto.y)
        forma.oeste.calcularPosicionDesdeEn(forma,unPunto)

    def __repr__(self):
        return "oeste"


class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"{COLOR.ORADOR} {alguien} entrando en la habitación {self.num} {COLOR.FIN}")
        alguien.posicion = self

    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def __repr__(self):
        return f" habitación {self.num}"
        #para que a la salida por consola no imprima la dir de memoria


class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print(COLOR.ALGOMALO + "te has chocado contra una pared" + COLOR.FIN)

    def __repr__(self):
        return "Pared"

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = True

    def entrar(self, ente):
        if self.activa:
            print(f"{COLOR.ALGOMALO} te has chocado contra una pared bomba {COLOR.FIN}")
            ente.vidas = ente.vidas - 1
            print(f"{ente} ha perdido 1 pto de vida. Vidas restantes: {ente.vidas}")
            if ente.vidas <= 0:
                ente.vidas = 0
                ente.estadoEnte.morir(ente)
            self.activa = False

    def esActiva(self):
        if self.activa:
            return COLOR.MONOLOGO + "Hmm, parece una pared normal y corriente... espero que no... explote..." + COLOR.FIN
        else:
            return COLOR.MONOLOGO + "Creo que es una pared... normal... como las demás..." + COLOR.FIN

    def activar_pared_bomba(self):
        self.activa = True

    def desactivar_pared_bomba(self):
        self.activa = False

    def __repr__(self):
        return "Pared bomba"


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.visitada = False
        self.estadoPuerta = Cerrada()

    def entrar(self, alguien):
        self.estadoPuerta.entrar(self, alguien)

    def puedeEntrar(self, alguien):
        print("Entrando en una puerta")
        if alguien.posicion == self.lado1:
            self.lado2.entrar(alguien)
        else:
            self.lado1.entrar(alguien)

    def abrir(self):
        print(COLOR.MONOLOGO + "Abro la puerta" + COLOR.FIN)
        self.estadoPuerta.abrir(self)

    def cerrar(self):
        print(COLOR.MONOLOGO + "Cierro la puerta" + COLOR.FIN)
        self.estadoPuerta.cerrar(self)

    def esPuerta(self):
        return True

    def aceptar(self, unVisitor):
        unVisitor.visitarPuerta(self)

    def calcularPosicionDesdeEn(self, forma, punto):
        print("punto: ", punto.x, punto.y)
        if self.visitada:
            return
        self.visitada = True
        if self.lado1.num == forma.num:
            self.lado2.forma.punto = punto
            self.lado2.calcularPosicion()
        else:
            self.lado1.forma.punto = punto
            self.lado1.calcularPosicion()

    def __repr__(self):
        if self.abierta:
            return "Puerta abierta"
        else:
            return "Puerta cerrada"


class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        #self.habitaciones = []

    def entrar(self, alguien):
        print(COLOR.ORADOR + "Bienvenido al laberinto" + COLOR.FIN)
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(alguien)

    def agregarHabitacion(self, hab):
        self.hijos.append(hab)

    def eliminarHabitacion(self, hab):
        if hab in self.hijos:
            self.hijos.remove(hab)
        else:
            print("No existe tal habitación")

    def obtenerHabitacion(self, num):
        for hab in self.hijos:
            if hab.num == num:
                return hab
        return None

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)

    def entrar(self, alguien):
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(alguien)
        print(f"{alguien} ha entrado en el laberinto")

    def aceptar(self, unVisitor):
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)


class Tunel(Hoja):
    def __init__(self, laberinto):
        super().__init__()
        self.laberinto = None

    def puedeClonarLaberinto(self, alguien):
        self.laberinto = alguien.juego.clonarLaberinto()
        self.laberinto.entrar(self)

    def entrar(self, alguien):
        if self.laberinto is None:
            alguien.clonarLaberinto(self)
        else:
            self.laberinto.entrar(alguien)

    def aceptar(self, unVisitor):
        unVisitor.visitarTunel(self)


class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    def fabricarJuego(self):
        self.juego = Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = copy.deepcopy(self.juego.laberinto)

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab = Habitacion(num)
        hab.forma = self.fabricarForma()
        hab.forma.num = num
        # hab.agregarOrientacion(self.fabricarNorte())
        # hab.agregarOrientacion(self.fabricarSur())
        # hab.agregarOrientacion(self.fabricarEste())
        # hab.agregarOrientacion(self.fabricarOeste())

        for i in hab.forma.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(), i)
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, obj1, lado2, obj2):
        hab1 = self.laberinto.obtenerHabitacion(lado1)
        hab2 = self.laberinto.obtenerHabitacion(lado2)
        puerta = Puerta(hab1, hab2)

        objOr1 = self.obtenerObjeto(obj1)
        objOr2 = self.obtenerObjeto(obj2)
        hab1.ponerElementoEnOrientacion(puerta, objOr1)
        hab2.ponerElementoEnOrientacion(puerta, objOr2)

    def obtenerObjeto(self, cadena):
        obj = None
        match cadena:
            case 'Norte':
                obj = self.fabricarNorte()
            case 'Sur':
                obj = self.fabricarSur()
            case 'Este':
                obj = self.fabricarEste()
            case 'Oeste':
                obj = self.fabricarOeste()
        return obj

    def fabricarForma(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())

        return forma

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = Agresivo()
        bicho.iniAgresivo()
        return bicho

    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = Perezoso()
        bicho.iniPerezoso()
        return bicho

    def obtenerJuego(self):
        return self.juego

    def fabricarBicho(self, modo, posicion):
        if modo=='Agresivo':
            bicho = self.fabricarBichoAgresivo()
        if modo=='Perezoso':
            bicho = self.fabricarBichoPerezoso()
        hab = self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(bicho)
        self.juego.agregarBicho(bicho)

    def fabricarTunelEn(self, unCont):
        tunel = Tunel(None)
        unCont.agregar_hijo(tunel)

# DECORATOR
class Decorator(Hoja):
    def __init__(self, elemento):
        super().__init__()
        self.elemento = elemento


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



# CREATOR
class Creator:

    def crearHabitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.forma = self.crearForma()
        pared_norte = self.crearPared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crearPared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crearPared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crearPared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion

    def crearForma(self):
        forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma


    def crear_laberinto(self):
        return Laberinto()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def crearPared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def crear_bomba(self, elemento):
        return Bomba(elemento)

    def crear_bicho(self, vidas, poder, posicion, modo):
        bicho = Bicho()
        bicho.vidas = vidas
        bicho.poder = poder
        bicho.posicion = posicion
        bicho.modo = modo
        return bicho

    def crear_bicho_agresivo(self):
        return Agresivo()

    def crear_bicho_perezoso(self):
        return Perezoso()


class CreatorB(Creator):
    def crear_pared_bomba(self):
        return ParedBomba()


# Modo de Bichos (Strategy)
class Modo:
    def __init__(self):
        pass

    def actuar(self, bicho):
        self.dormir(bicho)
        self.caminar(bicho)
        self.atacar(bicho)

    def dormir(self, bicho):
        pass

    def caminar(self, bicho):
        pass

    def atacar(self, bicho):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo está durmiendo. . ." + COLOR.FIN)
        time.sleep(5)

    def caminar(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo está caminando. . . agresivamente. . ." + COLOR.FIN)
        bicho.caminar()

    def atacar(self, bicho):
        print(COLOR.ORADOR + "Bicho agresivo ha atacado con furia titánica" + COLOR.FIN)
        bicho.atacar()

    def __str__(self):
        return "agresivo"

    def __repr__(self):
        return "agresivo"

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso duerme plácidamente. . . . ." + COLOR.FIN)
        time.sleep(10)

    def caminar(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso está... andando, o eso parece" + COLOR.FIN)
        bicho.caminar()

    def atacar(self, bicho):
        print(COLOR.ORADOR + "Bicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace" + COLOR.FIN)
        bicho.atacar()

    def __str__(self):
        return "perezoso"

    def __repr__(self):
        return "perezoso"

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()

    def clonarLaberinto(self, tunel):
        pass

    def esAtacadoPor(self, unAtacante):
        print(f"{COLOR.WARNINGACCION} Ataque {COLOR.FIN} : {self} está siendo atacado por {unAtacante}")
        self.vidas = self.vidas - unAtacante.poder
        print(f"{COLOR.ORADOR} Vidas restantes: {self.vidas} {COLOR.FIN}")
        if self.vidas == 0:
            print(f"{COLOR.ORADOR} El ente {self} ha muerto {COLOR.FIN}")
            self.estadoEnte.morir(self)

class Personaje(Ente):
    def __init__(self, vidas, poder, posicion, juego, nombre):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego = juego

    def clonarLaberinto(self, tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()

    def caminar(self):
        print(self.posicion.num)
        self.posicion.caminarAleatorio(self)
        print(f"El personaje {self} está caminando")

    def __repr__(self):
        return self.nombre


class EstadoEnte:
    def __init__(self):
        pass

    def vivir(self, ente):
        pass

    def morir(self, ente):
        pass

class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print(f"{COLOR.ORADOR} El ente está vivo {COLOR.FIN}")

    def morir(self, ente):
        print(f"{COLOR.ORADOR} El ente muere {COLOR.FIN}")
        ente.estadoEnte = Muerto()

class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print(f"{COLOR.ORADOR} El ente ha revivido {COLOR.FIN}")
        ente.estadoEnte = Vivo()

    def morir(self, ente):
        print(f"{COLOR.ORADOR} El ente ya está muerto {COLOR.FIN}")
        ente.juego.terminarJuego()


class EstadoPuerta:
    def __init__(self):
        pass

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print(f"{COLOR.ORADOR} La puerta ya está abierta {COLOR.FIN}")

    def cerrar(self, puerta):
        print(f"{COLOR.ORADOR} Cerrando la puerta {COLOR.FIN}")
        puerta.estadoPuerta = Cerrada()

    def entrar(self, puerta, alguien):
        puerta.puedeEntrar(alguien)

class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print(f"{COLOR.ORADOR} Abriendo la puerta {COLOR.FIN}")
        puerta.estadoPuerta = Abierta()

    def cerrar(self, puerta):
        print(f"{COLOR.ORADOR} La puerta ya está cerrada {COLOR.FIN}")

    def entrar(self, puerta, alguien):
        pass

class Bicho(Ente):
    def __init__(self):
        super().__init__()
        self.modo = None
        self.poder = None
        self.vidas = None
        self.posicion = None
        self.running = True

    def actua(self):
        while self.estaVivo():
            self.modo.actuar(self)

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def atacar(self):
        self.juego.buscarPersonaje(self)

    def caminar(self):
        self.posicion.caminarAleatorio(self)

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return f"Bicho {self.modo.__str__()}"

    def __repr__(self):
        return "Bicho -- vidas: {}, Poder: {}, Posicion: {}, Modo: {}".format(self.vidas, self.poder, self.posicion, self.modo)


class LaberintoGUI:
    def __init__(self, master, laberinto_file):
        self.master = master
        self.laberinto_file = laberinto_file
        self.juego = None
        self.canvas = None
        self.ancho = 0
        self.alto = 0

        self.load_laberinto()
        self.init_ui()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        self.juego.agregarPersonaje("Paco")

        self.personaje = self.juego.personaje
        self.bichos = self.juego.bichos

        for bicho in self.bichos:
            if isinstance(bicho.posicion, int):
                bicho.posicion = self.juego.obtenerHabitacion(bicho.posicion)

        print(f"Bichos cargados: {self.bichos}")

    def init_ui(self):
        self.master.title("El Laberinto")
        self.canvas = tk.Canvas(self.master, width=1280, height=720, bg = "white")
        self.canvas.pack()

        self.calcularLaberinto()
        for hab in self.juego.laberinto.hijos:
            print("num-punto", hab.num, hab.forma.punto.x, hab.forma.punto.y)
        self.dibujarLaberinto()
        self.dibujarPersonaje()
        self.dibujarBichos()

    def dibujarBichos(self):
        hab = self.personaje.posicion
        print(f"Posición personaje: {self.personaje.posicion}")
        print(f"personaje posicion num {self.personaje.posicion.num}")
        print("forma x personaje", hab.forma.punto.x)
        x = hab.forma.punto.x + hab.forma.extent.x // 2
        y = hab.forma.punto.y + hab.forma.extent.y // 2

        radio = 10
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue", outline="black")
        self.canvas.create_text(x, y - 15, text=self.personaje.nombre, fill="black", font=("Arial", 8))

    def dibujarBichos(self):
        colores = ["red", "green", "orange", "purple"]
        for idx, bicho in enumerate(self.bichos):
            # Resuelve la habitación a partir del número de la posición del bicho
            pos = bicho.posicion  # Aquí ya se debe tener la habitación correcta con las coordenadas transformadas
            hab = juego.obtenerHabitacion(pos)
            print("bicho posicion", bicho.posicion)
            print("bicho posicion num:", hab.num)
            print("forma x bichooo:", hab.forma.punto.x)
            print("forma y bichooo:", hab.forma.punto.y)

            x = hab.forma.punto.x + hab.forma.extent.x // 2
            y = hab.forma.punto.y + hab.forma.extent.y // 2

            offset = 15 * (idx % 4)  # Pequeño desplazamiento para evitar superposición
            radio = 8
            self.canvas.create_oval(x - radio + offset, y - radio + offset, x + radio + offset, y + radio + offset,
                                    fill=colores[idx % len(colores)], outline="black")
            self.canvas.create_text(x + offset, y + offset + 10, text=f"B{idx + 1}", fill="black", font=("Arial", 7))

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()

    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self)

    def visitarHabitacion(self, hab):
        self.dibujarRectangulo(hab.forma)

    def visitarPared(self, pared):
        pass
    def visitarPuerta(self, puerta):
        pass
    def visitarBomba(self, bomba):
        pass
    def visitarTunel(self, tunel):
        pass

    def dibujarRectangulo(self, forma):
        self.canvas.create_rectangle(forma.punto.x, forma.punto.y, forma.punto.x + forma.extent.x,
                                     forma.punto.y + forma.extent.y, fill="lightgray")

    def calcularPosicion(self):
        habitacion1 = self.juego.obtenerHabitacion(1)
        habitacion1.forma.punto = Point(0, 0)
        for habitacion in self.juego.laberinto.hijos:
            habitacion.calcularPosicion()

    def normalizar(self):
        min_x = 0
        min_y = 0

        # Buscar min_x y min_y
        for each in self.juego.laberinto.hijos:
            min_x = min(min_x, each.forma.punto.x)
            min_y = min(min_y, each.forma.punto.y)

        # Ajustar puntos
        for each in self.juego.laberinto.hijos:
            un_punto = each.forma.punto
            nuevo_x = un_punto.x + abs(min_x)
            nuevo_y = un_punto.y + abs(min_y)
            each.forma.punto = Point(nuevo_x, nuevo_y)

    def calcularTamContenedor(self):
        max_x = 0
        max_y = 0

        for each in self.juego.laberinto.hijos:
            max_x = max(max_x, each.forma.punto.x)
            max_y = max(max_y, each.forma.punto.y)

        max_x += 1
        max_y += 1

        self.ancho = round(1050 / max_x)
        self.alto = round(600 / max_y)

    def asignarPuntosReales(self):
        origen_x, origen_y = 70, 10

        for each in self.juego.laberinto.hijos:
            x = origen_x + (each.forma.punto.x * self.ancho)
            y = origen_y + (each.forma.punto.y * self.alto)

            each.forma.punto = Point(x, y)  # Asumo que Punto(x, y) es una clase
            each.forma.extent = Point(self.ancho, self.alto)

    # if __name__ == '__main__':
    #    root = tk.Tk()
    #    gui = LaberintoGUI(root, "./laberintos/lab4HabIzd4Bichos.json")  # Use a default laberinto file
    #    root.mainloop()

class LaberintoGUIVisitor(Visitor):
    def __init__(self, canvas):
        self.canvas = canvas

    def visitarLaberinto(self, laberinto):
        pass

    def visitarHabitacion(self, habitacion):
        x = habitacion.forma.point[0] if habitacion.forma.point else 0
        y = habitacion.forma.point[1] if habitacion.forma.point else 0
        self.canvas.create_rectangle(x, y, x + 40, y + 40, fill="lightgray")

    def visitarPared(self, pared):
        pass

    def visitarPuerta(self, puerta):
        pass

    def visitarBicho(self, bicho):
        pass

    def visitarOrientacion(self, orientacion):
        pass

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init


class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

    def obtenerJuego(self):
        return self.builder.obtenerJuego()

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarBichos()

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def iniBuilder(self):
        if self.dict['forma'] == 'cuadrado':
            self.builder=LaberintoBuilder()
#        elif self.dict['forma'] == 'cuadrado_modificado':
#            self.builder = LaberintoBuilderModificado()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each, 'root')

        # recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0], each[1], each[2], each[3])

    def fabricarLaberintoRecursivo(self,  each, padre):
        print(each)
        if each['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(each['num'])
        if each['tipo'] == 'tunel':
            self.builder.fabricarTunelEn(padre)
        if 'hijos' in each.keys():
            for cadaUno in each['hijos']:
                self.fabricarLaberintoRecursivo(cadaUno, con)

    def leerArchivo(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict = data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def fabricarBichos(self):
        for each in self.dict['bichos']:
            self.builder.fabricarBicho(each['modo'], each['posicion'])


# JUEGO
class Juego:
    def __init__(self):
        #self.laberinto = Laberinto()
        self.habitaciones = {}
        self.bichos = []
        self.bichos_threads = {}
        self.personaje = None
        self.prototipo = None
        self.runnning = True

    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)

    def agregarBicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

    def eliminarBicho(self, bicho):
        if bicho in self.bichos:
            self.bichos.remove(bicho)

    def hayBichosVivos(self):
        return any(b.estaVivo() for b in self.bichos)

    def lanzarBicho(self, bicho):
        thread = threading.Thread(target=bicho.actua)
        if bicho not in self.bichos_threads:
            self.bichos_threads[bicho] = []
        self.bichos_threads[bicho].append(thread)
        thread.start()

    def terminarBicho(self, bicho):
        if bicho in self.bichos_threads:
            for thread in self.bichos_threads[bicho]:
                bicho.vidas = 0
                bicho.running = False
                if thread is not threading.current_thread():
                    thread.join()
                self.bichos_threads.pop(bicho)
                self.bichos.remove(bicho)

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregarPersonaje(self, nombre):
        self.personaje = Personaje(20, 3, None, self, nombre)
        self.laberinto.entrar(self.personaje)

    def buscarPersonaje(self, bicho):
        if bicho.posicion.num == self.personaje.posicion.num:
            print(f"El bicho {bicho} ataca al personaje {self.personaje}")
            self.personaje.esAtacadoPor(bicho)

    def buscarBicho(self):
        for bicho in self.bichos:
            if bicho.posicion.num == self.personaje.posicion.num:
                print(f"El bicho {bicho} es atacado por {self.personaje}")
                bicho.esAtacadoPor(self.personaje)

    def abrirPuertas(self):
        def abrirPuertas(obj: Habitacion):
            objeto = obj.forma.este
            if objeto.esPuerta():
                print(f"Abriendo puerta", obj)
                objeto.abrir()
            objeto = obj.forma.oeste
            if objeto.esPuerta():
                print(f"Abriendo puerta", obj)
                objeto.abrir()
            objeto = obj.forma.norte
            if objeto.esPuerta():
                print(f"Abriendo puerta", obj)
                objeto.abrir()
            objeto = obj.forma.sur
            if objeto.esPuerta():
                print(f"Abriendo puerta", obj)
                objeto.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrarPuertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                print(f"Cerrando puerta {obj}")
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def iniciar_juego(self):
        pass

    def obtenerHabitacion(self, num):
        return self.laberinto.obtenerHabitacion(num)


    def crearLaberinto4habitaciones(self, creator):
        #   hab1  hab2
        #   hab3  hab4
        laberinto = creator.crear_laberinto()

        hab1 = creator.crearHabitacion(1)
        hab2 = creator.crearHabitacion(2)
        hab3 = creator.crearHabitacion(3)
        hab4 = creator.crearHabitacion(4)

        puerta12 = creator.crear_puerta(hab1, hab2)
        puerta24 = creator.crear_puerta(hab2, hab4)
        puerta43 = creator.crear_puerta(hab4, hab3)
        puerta31 = creator.crear_puerta(hab3, hab1)

        hab1.ponerElementoEnOrientacion(puerta12, Este())
        hab1.ponerElementoEnOrientacion(puerta31, Sur())
        hab2.ponerElementoEnOrientacion(puerta12, Oeste())
        hab2.ponerElementoEnOrientacion(puerta24, Sur())
        hab3.ponerElementoEnOrientacion(puerta43, Este())
        hab3.ponerElementoEnOrientacion(puerta31, Norte())
        hab4.ponerElementoEnOrientacion(puerta24, Norte())
        hab4.ponerElementoEnOrientacion(puerta43, Oeste())

        bicho1 = creator.crear_bicho(5, 10, hab1, creator.crear_bicho_agresivo())
        self.agregarBicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, hab3, creator.crear_bicho_agresivo())
        self.agregarBicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, hab2, creator.crear_bicho_perezoso())
        self.agregarBicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, hab4, creator.crear_bicho_perezoso())
        self.agregarBicho(bicho4)

        hab1.bicho = bicho1
        hab2.bicho = bicho2
        hab3.bicho = bicho3
        hab4.bicho = bicho4

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        laberinto.agregarHabitacion(hab3)
        laberinto.agregarHabitacion(hab4)

        return laberinto

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()

        hab1 = creator.crearHabitacion(1)
        hab2 = creator.crearHabitacion(2)

        puerta12 = creator.crear_puerta(hab1, hab2)

        hab1.ponerElementoEnOrientacion(puerta12, Norte())
        hab2.ponerElementoEnOrientacion(puerta12, Sur())

        paredB1 = creator.crear_pared_bomba()
        paredB2 = creator.fabricar_pared_bomba()

        hab1.ponerElementoEnOrientacion(paredB1, Sur())
        hab2.ponerElementoEnOrientacion(paredB2, Norte())

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

        return laberinto

    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.fabricar_laberinto()
        hab1 = creator.fabricar_habitacion(1)
        hab2 = creator.fabricar_habitacion(2)
        puerta = creator.fabricar_puerta(hab1, hab2)

        hab1.sur = puerta
        hab2.norte = puerta

        pared1 = creator.fabricar_pared()
        bomba1 = creator.fabricar_bomba(pared1)
        hab1.este = bomba1

        pared2 = creator.fabricar_pared()
        bomba2 = creator.fabricar_bomba(pared2)
        hab2.oeste = bomba2

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        return laberinto

    def terminarJuego(self):
        self.terminarBichos()



if __name__ == "__main__":
    fm = Creator()
    juego = Juego()
    juego.laberinto = juego.crearLaberinto4habitaciones(fm)


    print("\n\nLaberinto 4 habitaciones\n")

    for hab in juego.laberinto.hijos:
        print(f"Habitación: {hab.num}")
    print()
    for bicho in juego.bichos:
        print(bicho)
        print(f"Bicho con {bicho.vidas} pts de vida y {bicho.poder} pts de poder")
        print(f"Posición (habitación) del bicho: {bicho.posicion.num}")
        print()

    # juego.laberinto.recorrer(print)