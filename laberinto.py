from contenedor import Contenedor
from color import COLOR

class Laberinto(Contenedor):
    def __init__(self):
        super().__init__()
        #self.habitaciones = []

    def entrar(self, alguien):
        print(COLOR.ORADOR + "\n \n \nBienvenido al laberinto" + COLOR.FIN)
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
        for hijo in self.hijos:
            func(hijo)
            hijo.recorrer(func)


    def aceptar(self, unVisitor):
        for hijo in self.hijos:
            hijo.aceptar(unVisitor)