from habitacion import Habitacion
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste
from ente import Personaje, Vivo, Muerto
from color import COLOR

import time
import copy
import sys

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
        import threading
        if bicho not in self.bichos_threads:
            thread = threading.Thread(target=bicho.actua) #daemon=True
            self.bichos_threads[bicho] = []
        self.bichos_threads[bicho].append(thread)
        thread.start()

    def terminarBicho(self, bicho):
        import threading
        if bicho in self.bichos_threads:
            for thread in self.bichos_threads[bicho]:
                bicho.vidas = 0
                bicho.running = False
                if thread is not threading.current_thread():
                    thread.join(timeout=2)
                try:
                    self.bichos_threads.pop(bicho)
                    self.bichos.remove(bicho)
                except Exception:
                    print("Bicho ya eliminado")

    def lanzarBichos(self):
        for bicho in self.bichos:
            self.lanzarBicho(bicho)

    def terminarBichos(self):
        for bicho in self.bichos:
            self.terminarBicho(bicho)

    def agregarPersonaje(self, nombre):
        self.personaje = Personaje(30, 7, None, self, nombre)
        self.laberinto.entrar(self.personaje)

    def buscarPersonaje(self, bicho):
        if bicho.posicion.num == self.personaje.posicion.num:
            print(f"El personaje {bicho} ataca al personaje {self.personaje}")
            self.personaje.esAtacadoPor(bicho)

    def buscarBicho(self):
        for bicho in self.bichos:
            if bicho.posicion.num == self.personaje.posicion.num:
                print(f"El bicho {bicho} es atacado por el personaje {self.personaje}")
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
        # LOGICA
        pass

    def terminarJuego(self):
        self.terminarBichos()
        #os.kill(os.getpid(), signal.SIGTERM)
        time.sleep(1)
        if self.personaje.vidas > 0:
            print(f"\n🎉 {COLOR.ORADOR} ¡{self.personaje.nombre} ha ganado el juego! {COLOR.FIN}")
        else:
            print(f"\n💀 {COLOR.ALGOMALO} {self.personaje.nombre} ha muerto. ¡Los bichos ganan! {COLOR.FIN}")
        sys.exit()



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



    def crearLaberinto4habitacionesImplementaciones(self, creator):
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

        hojaTotem = creator.crearTotem()
        hojaBolsa = creator.crearBolsa()
        hab2.agregarHijo(hojaTotem)
        hab3.agregarHijo(hojaBolsa)

        hab1.bicho = bicho1
        hab2.bicho = bicho2
        hab3.bicho = bicho3
        hab4.bicho = bicho4

        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)
        laberinto.agregarHabitacion(hab3)
        laberinto.agregarHabitacion(hab4)

        return laberinto