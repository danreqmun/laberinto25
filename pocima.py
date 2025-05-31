from color import COLOR
from hojaObjetos import HojaObjeto
from inventarioHandler import InventarioHandler

class Pocima(HojaObjeto, InventarioHandler):
    def __init__(self):
        HojaObjeto.__init__(self, nombre="Pócima de escudo", peso=1)
        InventarioHandler.__init__(self)

    def usar(self, personaje):
        if self.es_usable(personaje):
            self.aplicarEfecto(personaje)
            print(f"{COLOR.MONOLOGO} ({personaje.nombre}) voy a usar {COLOR.FIN} {COLOR.MORADO} {self.nombre} {COLOR.FIN}. . .")
            print(f"{COLOR.ORADOR} Vidas de {personaje.nombre} aumentadas a {personaje.vidas}")

    def es_usable(self, personaje):
        return personaje.vidas > 0

    def aplicarEfecto(self, personaje):
        personaje.vidas = personaje.vidas + 5

    def manejar(self, personaje, nombre_obj, inventario):
        if self.nombre == nombre_obj:
            self.usar(personaje)
            #inventario.objetosBolsa.remove(self)
            return True
        return super().manejar(personaje, nombre_obj, inventario)