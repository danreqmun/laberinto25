""" 12 febrero """

from abc import ABC, abstractmethod


class ElementoMapa(ABC):
    @abstractmethod
    def entrar(self):
        pass


class Habitacion(ElementoMapa):
    def __init__(self):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num = None

    def entrar(self):
        print(f"Has entrado a la habitación {self.num}")


class Pared(ElementoMapa):
    def entrar(self):
        print("Te has chocado contra una pared")

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    def entrar(self):
        if self.abierta:
            print("Has pasado a la siguiente habitación")
        else:
            print("Te has chocado contra la puerta, está cerrada")

class Laberinto(Habitacion):
    def __init__(self):
        self.habitaciones = list()

    def agregarHabitacion(self, hab):
        self.habitaciones.append(hab)

    def eliminarHabitacion(self, hab):
        if hab in self.habitaciones:
            self.habitaciones.remove(hab)
        else:
            print("No existe ese objeto habitación")



class Juego:
    def __init__(self):
        self.laberinto = None

    def crearPared(self):
        return Pared()

    def crearPuerta(self, abierta, lado1, lado2):
        puerta = Puerta()
        puerta.abierta = True
        puerta.lado1 = lado1
        puerta.lado2 = lado2

        return puerta

    def crearHabitacion(self, num):
        habitacion = Habitacion()
        habitacion.num = num
        habitacion.norte = self.crearPared()
        habitacion.sur = self.crearPared()
        habitacion.este = self.crearPared()
        habitacion.oeste = self.crearPared()
        return habitacion


    def crearLaberinto2Habitaciones(self):
