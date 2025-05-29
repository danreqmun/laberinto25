from color import COLOR
from hojaObjetos import HojaObjeto
from estadoEnte import Vivo
from inventarioHandler import InventarioHandler

# template method
class Totem(HojaObjeto, InventarioHandler):
    def __init__(self):
        HojaObjeto.__init__(self, nombre="Tótem de la inmortalidad", peso=2)
        InventarioHandler.__init__(self)

    def usar(self, personaje):
        if self.es_usable(personaje):
            self.aplicarEfecto(personaje)
            print(f"{COLOR.ORADOR} {personaje.nombre} ha usado el Tótem de la inmortalidad... {COLOR.BLANCO} ¡HA REVIVIDO! {COLOR.FIN}")

    def es_usable(self, personaje):
        return personaje.vidas <= 0

    def aplicarEfecto(self, personaje):
        personaje.estadoEnte = Vivo()
        personaje.vidas = 20
        personaje.poder = 12

    def manejar(self, personaje, nombre_obj, inventario):
        if self.nombre == nombre_obj:
            self.usar(personaje)
            inventario.eliminar(self)
            return True
        return super().manejar(personaje, nombre_obj, inventario)