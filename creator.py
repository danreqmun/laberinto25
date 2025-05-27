from agresivo import Agresivo
from bicho import Bicho
from bomba import Bomba
from hojaObjetos import Totem, Pocima
from juego import Habitacion
from laberinto import Laberinto
from norte import Norte
from objetosMapa import Bolsa
from pared import Pared
from paredBomba import ParedBomba
from perezoso import Perezoso
from puerta import Puerta
from sur import Sur
from este import Este
from oeste import Oeste
from orientacion import Orientacion
from cuadrado import Cuadrado

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


    # IMPLEMENTACIONES
    def crearTotem(self):
        return Totem()

    def crearPocima(self):
        return Pocima()

    def crearBolsa(self):
        bolsa = Bolsa()
        bolsa.agregar(Pocima())
        bolsa.agregar(Pocima())
        return bolsa


class CreatorB(Creator):
    def crear_pared_bomba(self):
        return ParedBomba()
