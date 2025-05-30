from contenedor import Contenedor
from ente import Personaje, Vivo
from color import COLOR
from objetosMapa import ObjetosMapa

class Habitacion(Contenedor):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def entrar(self, alguien):
        print(f"{COLOR.ORADOR} {alguien} ha entrado en la habitación {self.num} {COLOR.FIN}")
        alguien.posicion = self

        if isinstance(alguien, Personaje) and alguien.vidas > 0:
            for hijo in list(self.hijos):
            #for hijo in alguien.posicion.hijos[:]:
                if isinstance(hijo, ObjetosMapa):
                    hijo.recoger(alguien)
                    self.hijos.remove(hijo)



    def visitarContenedor(self, unVisitor):
        unVisitor.visitarHabitacion(self)

    def calcularPosicion(self):
        self.forma.calcularPosicion()

    def __repr__(self):
        return f" habitación {self.num}"
        #para que a la salida por consola no imprima la dir de memoria