from flyweight import Flyweight
from objetosMapa import ObjetosMapa

class Moneda(Flyweight):
    def __init__(self, tipo, peso):
        Flyweight.__init__(self)
        ObjetosMapa.__init__(self, f"Moneda de {tipo}")
        self.tipo = tipo #estado intrínseco (compartido)
        self.peso = peso

    def devPeso(self):
        return self.peso

    def recoger(self, personaje):
        from ente import Personaje
        if isinstance(personaje, Personaje):
            personaje.inventario.agregar(self)