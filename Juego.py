
""" 25/03/25 """

import threading
import time


class COLOR:
    FIN = '\033[0m'   # hay que ponerlo al final de cada frase o si no el resto del programa usará el color anterior
    AMARILLO = '\033[93m' # orador
    ROJO = '\033[91m'     # algo malo
    AZUL = '\033[94m'     # monologo

# FACTORY METHOD --- COMPONENT
class ElementoMapa:
    def __init__(self):
        self.padre = None

    def entrar(self):
        pass

    def recorrer(self, func):
        func(self)

    def esPuerta(self):
        return False


# COMPOSITE
class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
        self.orientaciones = []

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def eliminar_hijo(self, hijo):
        self.hijos.remove(hijo)

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)
        for orientacion in self.orientaciones:
            orientacion.recorrer(func, self)

# LEAF
class Hoja(ElementoMapa):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Soy una hoja"

# SINGLETON
class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        pass

class Norte(Orientacion):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def poner(self, elemento, contenedor):
        contenedor.norte(elemento)

    def recorrer(self, func, contenedor):
        if contenedor.norte is not None:
            func(contenedor.norte)

    def __repr__(self):
        return "norte"

class Sur(Orientacion):
    def poner(self, elemento, contenedor):
        contenedor.sur(elemento)

    def recorrer(self, func, contenedor):
        if contenedor.sur is not None:
            func(contenedor.sur)

class Este(Orientacion):
    def poner(self, elemento, contenedor):
        contenedor.este(elemento)

    def recorrer(self, func, contenedor):
        if contenedor.este is not None:
            func(contenedor.este)

class Oeste(Orientacion):
    def poner(self, elemento, contenedor):
        contenedor.oeste(elemento)

    def recorrer(self, func, contenedor):
        if contenedor.oeste is not None:
            func(contenedor.oeste)




class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"entrando en la habitación {self.num}")
        alguien.posicion = self

    def __repr__(self):
        return f" habitación {self.num}"
        #para que a la salida por consola no imprima la dir de memoria


class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print(COLOR.ROJO + "te has chocado contra una pared" + COLOR.FIN)

    def __repr__(self):
        return "Pared"

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print( COLOR.ROJO + "te has chocado contra una pared bomba" + COLOR.FIN)

    def is_activa(self):
        if self.activa:
            return COLOR.AZUL + "Hmm, parece una pared normal y corriente... espero que no... explote..." + COLOR.FIN
        else:
            return COLOR.AZUL + "Creo que es una pared... normal... como las demás..." + COLOR.FIN

    def activar_pared_bomba(self):
        self.activa = True

    def __repr__(self):
        return "Pared bomba"


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self):
        if self.abierta:
            print(f"puerta {self.lado1.num} - {self.lado2.num} está abierta, paso")
        else:
            print(f"puerta  {self.lado1.num} - {self.lado2.num} está cerrada, no puedo pasar")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def __repr__(self):
        if self.abierta:
            return "Puerta abierta"
        else:
            return "Puerta cerrada"


class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def entrar(self, alguien):
        print(COLOR.AMARILLO + "Bienenido al laberinto" + COLOR.FIN)
        hab1 = self.obtener_habitacion(1)
        hab1.entrar(alguien)

    def agregar_habitacion(self, hab):
        self.habitaciones.append(hab)

    def eliminar_habitacion(self, hab):
        if hab in self.habitaciones:
            self.habitaciones.remove(hab)
        else:
            print("no existe tal habitación")

    def obtener_habitacion(self, num):
        for hab in self.habitaciones:
            if hab.num == num:
                return hab
        return None

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)

class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego = None

    def fabricarJuego(self):
        self.juego = Juego()
        self.juego.laberinto = self.laberinto

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab = Habitacion(num)
        hab.agregarOrientacion(self.fabricarNorte())
        hab.agregarOrientacion(self.fabricarSur())
        hab.agregarOrientacion(self.fabricarEste())
        hab.agregarOrientacion(self.fabricarOeste())
        for each in hab.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(), each)
        self.laberinto.agregar_habitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, or1, lado2, or2):
        hab1 = self.laberinto.obtener_habitacion(lado1)
        hab2 = self.laberinto.obtener_habitacion(lado2)
        puerta = Puerta(lado1, lado2)
        objOr1 = self.obtenerObjeto(or1)
        objOr2 = self.obtenerObjeto(or2)
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
        hab = self.laberinto.obtener_habitacion(posicion)
        hab.entrar(bicho)
        self.juego.agregar_habitacion(bicho)

# DECORATOR (Bomba en Pared)
class Decorator(ElementoMapa):
    def __init__(self, elemento):
        self.elemento = elemento


class Bomba(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = False

    def __repr__(self):
        return "Bomba"

    def activar_bomba(self):
        self.activa = True



# CREATOR
class Creator:

    def crear_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.orientaciones.append(self.crear_norte())
        habitacion.orientaciones.append(self.crear_sur())
        habitacion.orientaciones.append(self.crear_este())
        habitacion.orientaciones.append(self.crear_oeste())
        pared_norte = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_norte, Norte())
        pared_sur = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_sur, Sur())
        pared_este = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_este, Este())
        pared_oeste = self.crear_pared()
        habitacion.ponerElementoEnOrientacion(pared_oeste, Oeste())
        return habitacion


    def crear_laberinto(self):
        return Laberinto()

    def crear_pared(self):
        return Pared()

    def crear_norte(self):
        return Norte()

    def crear_sur(self):
        return Sur()

    def crear_este(self):
        return Este()

    def crear_oeste(self):
        return Oeste()


    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)


    def crear_bomba(self, elemento):
        return Bomba(elemento)

    def crear_bicho(self):
        return Bicho()

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
        print("Bicho agresivo está durmiendo. . .")
        time.sleep(2)

    def caminar(self, bicho):
        print("Bicho agresivo está caminando. . . agresivamente. . .")

    def atacar(self, bicho):
        print("Bicho agresivo ha atacado con furia espartana")

    def __repr__(self):
        return "agresivo"

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Bicho perezoso duerme plácidamente. . . . .")
        time.sleep(10)

    def caminar(self, bicho):
        print("Bicho perezoso está... andando, o eso parece")

    def atacar(self, bicho):
        print("Bicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace")

    def __repr__(self):
        return "perezoso"

class Bicho:
    def __init__(self, vidas, poder, modo, posicion):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = posicion

    def actua(self):
        while self.estaVivo():
            self.modo.actuar()

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return f"Bicho --- vidas: {self.vidas}, Poder: {self.poder}, Posicion: {self.posicion}, Modo: {self.modo}"

    def __repr__(self):
        return "Bicho -- vidas: {}, Poder: {}, Posicion: {}, Modo: {}".format(self.vidas, self.poder, self.posicion, self.modo)

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None

class Personaje(Ente):
    def __init__(self, vidas, poder, posicion, juego, nombre):
        self.nombre = nombre

# JUEGO
class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []
        self.bichos_threads = {}

    def agregar_bicho(self, bicho):
        bicho.juego = self
        self.bichos.append(bicho)

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

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregar_personaje(self, nombre):
        self.personaje = Personaje(10, 1, None, self, nombre)
        self.laberinto.entrar(self.personaje)

    def abrirPuertas(self):
        def abrirPuertas(obj):
            if obj.esPuerta():
                obj.abrir()
        self.laberinto.recorrer(abrirPuertas)

    def cerrarPuertas(self):
        def cerrarPuertas(obj):
            if obj.esPuerta():
                obj.cerrar()
        self.laberinto.recorrer(cerrarPuertas)

    def iniciar_juego(self):
        pass

    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)


    def crearLaberinto4habitaciones(self, creator):
        #   hab1  hab2
        #   hab3  hab4
        laberinto = creator.crear_laberinto()

        hab1 = creator.crear_habitacion(1)
        hab2 = creator.crear_habitacion(2)
        hab3 = creator.crear_habitacion(3)
        hab4 = creator.crear_habitacion(4)

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

        bicho1 = creator.crear_bicho(5, 10, creator.fabricar_bicho_agresivo(), hab1)
        self.agregar_bicho(bicho1)
        bicho3 = creator.crear_bicho(5, 10, creator.fabricar_bicho_agresivo(), hab3)
        self.agregar_bicho(bicho3)
        bicho2 = creator.crear_bicho(5, 1, creator.fabricar_bicho_perezoso(), hab2)
        self.agregar_bicho(bicho2)
        bicho4 = creator.crear_bicho(5, 1, creator.fabricar_bicho_perezoso(), hab4)
        self.agregar_bicho(bicho4)

        hab1.bicho = bicho1
        hab2.bicho = bicho2
        hab3.bicho = bicho3
        hab4.bicho = bicho4

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        return laberinto

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.crear_laberinto()

        hab1 = creator.crear_habitacion(1)
        hab2 = creator.crear_habitacion(2)

        puerta12 = creator.crear_puerta(hab1, hab2)

        hab1.ponerElementoEnOrientacion(puerta12, Norte())
        hab2.ponerElementoEnOrientacion(puerta12, Sur())

        paredB1 = creator.crear_pared_bomba()
        paredB2 = creator.fabricar_pared_bomba()

        hab1.ponerElementoEnOrientacion(paredB1, Sur())
        hab2.ponerElementoEnOrientacion(paredB2, Norte())

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)

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

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto



if __name__ == "__main__":
    fm = Creator()
    juego = Juego()
    juego.laberinto = juego.crearLaberinto2HabFM(fm)
    hab1 = juego.obtenerHabitacion(1)
    hab2 = juego.obtenerHabitacion(2)

    print("\n\nLaberinto 2 habitaciones con pared bomba\n")

    for hab in juego.laberinto.habitaciones:
        print(f"Habitación: {hab.num}")
        print(f"Norte: {hab.norte}, Sur: {hab.sur}, Este: {hab.este}, Oeste: {hab.oeste}")
        if hasattr(hab, "bicho"):
            bicho = hab.bicho
            print(
                f"Bicho --- vidas: {bicho.vidas}, Poder: {bicho.poder}, Posicion: {bicho.posicion}, Modo: {bicho.modo}")

        print("\n")
