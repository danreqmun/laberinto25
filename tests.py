import random
import unittest

from bolsa import Bolsa
from bomba import Bomba
from estadoEnte import Vivo
from flecha import Flecha
from juego import Juego
from monedaFactory import MonedaFactory
from sur import Sur
from creator import Creator, CreatorB, CreatorF
from paredBomba import ParedBomba
from paredFlecha import ParedFlecha
from ente import Ente, Personaje
from pocima import Pocima
from totem import Totem
from moneda import Moneda


class Tests(unittest.TestCase):
    def test_factory_method(self):
        juego = Juego()
        fmb = CreatorB()
        fmf = CreatorF()
        laberinto = juego.pruebasCrearLaberinto2HabFM(fmb, fmf)

        hab1 = laberinto.obtenerHabitacion(1)
        hab2 = laberinto.obtenerHabitacion(2)

        pared_sur_hab1 = hab1.obtenerElementoEnOrientacion(Sur())
        pared_sur_hab2 = hab2.obtenerElementoEnOrientacion(Sur())


        self.assertEqual(pared_sur_hab1.__class__, ParedBomba)
        self.assertEqual(pared_sur_hab2.__class__, ParedFlecha)

    def test_decorators(self):
        juego = Juego()
        fm = Creator()
        juego.laberinto = juego.pruebasCrearLaberinto2HabDecorators(fm)

        hab1 = juego.obtenerHabitacion(1)
        hab2 = juego.obtenerHabitacion(2)

        pared_sur_hab1 = hab1.obtenerElementoEnOrientacion(Sur())
        pared_sur_hab2 = hab2.obtenerElementoEnOrientacion(Sur())

        self.assertEqual(pared_sur_hab1.__class__, Bomba)
        self.assertEqual(pared_sur_hab2.__class__, Flecha)

    def test_pocima(self):
        p = Personaje(5, 2, None, None, "Conejillo de Indias")
        p.inventario.agregar(Pocima())
        p.inventario.usar(p, "Pócima de escudo")

        self.assertEqual(p.vidas, 10)

    def test_totem(self):
        p = Personaje(0, 2, None, None, "Conejillo de Indias")
        p.inventario.agregar(Totem())
        p.inventario.usar(p, "Tótem de la inmortalidad")

        self.assertEqual(p.estadoEnte.__class__, Vivo().__class__)
        #hay que comparar la clase. Si no, cada Vivo() tiene una dir de memoria diferente
        self.assertEqual(p.vidas, 20)
        self.assertEqual(p.poder, 12)

    def test_bolsa(self):
        p = Personaje(5, 2, None, None, "Conejillo de Indias")
        bolsa = Bolsa()
        bolsa.agregar(Pocima())
        p.inventario.agregar(bolsa)
        p.inventario.usar(p, "Pócima de escudo")

        self.assertEqual(p.vidas, 10)

    def test_recoger_moneda(self):
        juego = Juego()
        fm = Creator()
        juego.laberinto = juego.pruebasCrearLaberinto1Hab(fm)

        hab = juego.obtenerHabitacion(1)

        oro = MonedaFactory.getMoneda("oro")
        o = random.randint(2, 4)
        for _ in range(o):
            hab.agregarHijo(oro)

        p = Personaje(10, 10, hab, juego, "Conejillo de Indias")
        for hijo in list(p.posicion.hijos):
            if isinstance(hijo, Moneda):
                hijo.recoger(p)
                p.posicion.hijos.remove(hijo)
        self.assertTrue(p.inventario.tiene_objeto(Moneda))