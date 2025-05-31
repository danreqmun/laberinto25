import unittest

from bomba import Bomba
from flecha import Flecha
from juego import Juego
from sur import Sur
from creator import Creator, CreatorB, CreatorF
from paredBomba import ParedBomba
from paredFlecha import ParedFlecha

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