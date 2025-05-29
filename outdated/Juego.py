
""" 22/04/25 """
import copy
import json
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


class Forma:
    def __init__(self):
        self.orientaciones = []

    def agregarOrientacion(self, orientacion):
        self.orientaciones.append(orientacion)

    def eliminarOrientacion(self, orientacion):
        self.orientaciones.remove(orientacion)

    def ponerElementoEnOrientacion(self, elemento, orientacion):
        orientacion.poner(elemento, self)

    def obtenerElementoEnOrientacion(self, orientacion):
        return orientacion.obtenerElemento(self)


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

    def __str__(self):
        return " hoja"


# SINGLETON
class Orientacion:
    def __init__(self):
        pass

    def poner(self, elemento, contenedor):
        pass

    def obtenerElemento(self, forma):
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

    def __repr__(self):
        return "oeste"


class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(COLOR.AMARILLO + f"entrando en la habitación {self.num}" + COLOR.FIN)
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

    def esActiva(self):
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

    def entrar(self, alguien):
        if self.abierta:
            if alguien.posicion == self.lado1:
                self.lado2.entrar(alguien)
                print(f"{COLOR.AZUL} puerta {self.lado1.num} - {self.lado2.num} está abierta, paso {COLOR.FIN}")
            else:
                self.lado1.entrar(alguien)
                print(f"{COLOR.AZUL} puerta {self.lado2.num} - {self.lado1.num} está abierta, paso {COLOR.FIN}")
        else:
            print(COLOR.AMARILLO + "la puerta está cerrada, no puedo pasar" + COLOR.FIN)

    def abrir(self):
        print(COLOR.AZUL + "Abro la puerta" + COLOR.FIN)
        self.abierta = True

    def cerrar(self):
        print(COLOR.AZUL + "Cierro la puerta" + COLOR.FIN)
        self.abierta = False

    def esPuerta(self):
        return True

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
        print(COLOR.AMARILLO + "Bienenido al laberinto" + COLOR.FIN)
        hab1 = self.obtenerHabitacion(1)
        hab1.entrar(alguien)

    def agregarHabitacion(self, hab):
        self.hijos.append(hab)

    def eliminarHabitacion(self, hab):
        if hab in self.habitaciones:
            self.hijos.remove(hab)
        else:
            print("no existe tal habitación")

    def obtenerHabitacion(self, num):
        for hab in self.habitaciones:
            if hab.num == num:
                return hab
        return None

    def recorrer(self, func):
        func(self)
        for hijo in self.hijos:
            hijo.recorrer(func)


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

        for i in hab.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(), i)
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, obj1, lado2, obj2):
        hab1 = self.laberinto.obtenerHabitacion(lado1)
        hab2 = self.laberinto.obtenerHabitacion(lado2)
        puerta = Puerta(lado1, lado2)

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

    def activar_bomba(self):
        self.activa = True

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
        forma=Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma


    def crear_laberinto(self):
        return Laberinto()

    def crearPared(self):
        return Pared()

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()


    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)


    def crear_bomba(self, elemento):
        return Bomba(elemento)

    def crear_bicho(self, vidas, poder, posicion, modo):
        bicho=Bicho()
        bicho.vidas=vidas
        bicho.poder=poder
        bicho.posicion=posicion
        bicho.modo=modo
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
        print(COLOR.AMARILLO + "Bicho agresivo está durmiendo. . ." + COLOR.FIN)
        time.sleep(2)

    def caminar(self, bicho):
        print(COLOR.AMARILLO + "Bicho agresivo está caminando. . . agresivamente. . ." + COLOR.FIN)

    def atacar(self, bicho):
        print(COLOR.AMARILLO + "Bicho agresivo ha atacado con furia espartana" + COLOR.FIN)

    def __repr__(self):
        return "agresivo"

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(COLOR.AMARILLO + "Bicho perezoso duerme plácidamente. . . . ." + COLOR.FIN)
        time.sleep(10)

    def caminar(self, bicho):
        print(COLOR.AMARILLO + "Bicho perezoso está... andando, o eso parece" + COLOR.FIN)

    def atacar(self, bicho):
        print(COLOR.AMARILLO + "Bicho perezoso intenta atacar pero. . . eso es mucho trabajo, no lo hace" + COLOR.FIN)

    def __repr__(self):
        return "perezoso"

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None

    def clonarLaberinto(self, tunel):
        pass

class Personaje(Ente):
    def __init__(self, vidas, poder, posicion, juego, nombre):
        self.nombre = nombre

    def clonarLaberinto(self, tunel):
        tunel.puedeClonarLaberinto()

class Bicho(Ente):
    def __init__(self):
        self.modo = None
        self.poder = None
        self.vidas = None
        self.posicion = None

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
        if self.dict['forma']=='cuadrado':
            self.builder=LaberintoBuilder()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each, 'root')

        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0], each[1], each[2], each[3])

            # recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0], each[1], each[2], each[3])

        def fabricarLaberintoRecursivo(self,  each, padre):
            print(each)
            if each['tipo'] == 'habitacion':
                con = self.builder.fabricarHabitacion(each['num'])

            if each['hijos'] != None:
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

    def clonarLaberinto(self):
        return copy.deepcopy(self.prototipo)

    def agregarBicho(self, bicho):
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
            for bicho in self.bichos_threads[bicho]:
                bicho.vidas = 0

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregarPersonaje(self, nombre):
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



if __name__ == "__main__":
    fm = Creator()
    juego = Juego()
    juego.laberinto = juego.crearLaberinto4habitaciones(fm)


    print("\n\nLaberinto 4 habitaciones\n")

    for hab in juego.laberinto.hijos:
        print(f"Habitación: {hab.num}")

    for bicho in juego.bichos:
        print(bicho)
        print(f"Bicho con {bicho.vidas} pts de vida y {bicho.poder} pts de poder")
        print(f"Posición del bicho: {bicho.posicion.num}")

    #juego.laberinto.recorrer(print)
