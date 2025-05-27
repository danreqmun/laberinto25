from objetosMapa import ObjetosMapa
from estadoEnte import Vivo, Muerto

class HojaObjeto(ObjetosMapa):
    def __init__(self, nombre, peso):
        super().__init__(nombre)
        self._peso = peso

    def usar(self, personaje):
        pass

    def es_usable(self, personaje):
        pass

    def aplicarEfecto(self, personaje):
        pass

    def recoger(self, personaje):
        personaje.inventario.agregar(self)

    def devPeso(self):
        return self._peso

# template method
class Totem(HojaObjeto):
    def __init__(self):
        super().__init__("Tótem de la inmortalidad", peso=2)

    def usar(self, personaje):
        if self.es_usable(personaje):
            self.aplicarEfecto(personaje)

    def es_usable(self, personaje):
        return isinstance(personaje.estadoEnte, Muerto)

    def aplicarEfecto(self, personaje):
        #personaje.estadoEnte = Muerto # ya se comprueba en es_usable en este caso
        personaje.estadoEnte.vivir(personaje)  # Estado Muerto.vivir revive al personaje
        personaje.vidas = 20
        personaje.poder = 12



class Pocima(HojaObjeto):
    def __init__(self):
        super().__init__("Pocima de escudo", peso=1)

    def usar(self, personaje):
        if self.es_usable(personaje):
            self.aplicarEfecto(personaje)

    def es_usable(self, personaje):
        return isinstance(personaje.estadoEnte, Vivo)

    def aplicarEfecto(self, personaje):
        personaje.vidas += 3