from creator import Creator
from creator import CreatorB,CreatorC
from juego import Juego
from este import Este
from oeste import Oeste
import time


fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto2HabFM(fm)
hab1=juego.obtenerHabitacion(1)
hab2=juego.obtenerHabitacion(2)
print(hab1.num)
print(hab2.num)