from objetosMapa import ObjetosMapa
from inventarioHandler import InventarioHandler

class Bolsa(ObjetosMapa, InventarioHandler):
    def __init__(self, nombre = "Bolsa"):
        ObjetosMapa.__init__(self, nombre)
        InventarioHandler.__init__(self)
        self.objetosBolsa = []

    def manejar(self, personaje, nombre_obj, inventario):
        if self.nombre == nombre_obj:
            print("No puedes usar la bolsa directamente")
            return False

        # recorrer los objetos dentro de la bolsa
        for obj in self.objetosBolsa:
            if isinstance(obj, InventarioHandler):
                if obj.manejar(personaje, nombre_obj, inventario):
                    #self.objetosBolsa.remove(obj) # aquí es donde se elimina
                    inventario.eliminar(obj)
                    return True

        # no estaba en la bolsa, pasa al siguiente handler
        return super().manejar(personaje, nombre_obj, inventario)

    def agregar(self, obj):
        if isinstance(obj, ObjetosMapa):
            self.objetosBolsa.append(obj)
        else:
            print(f"Esto no es un objeto del mapa")

    def recoger(self, personaje):
        from ente import Personaje
        if isinstance(personaje, Personaje):
            personaje.inventario.agregar(self)


    def usar(self, personaje):
        print(f"Usando el contenido de la bolsa '{self.nombre}':")
        for obj in self.objetosBolsa:
            obj.usar(personaje)

    def devPeso(self):
        return sum(obj.devPeso() for obj in self.objetosBolsa)