from bolsa import Bolsa
from color import COLOR
from inventarioHandler import InventarioHandler


class Inventario:
    def __init__(self, peso_maximo):
        self.peso_maximo = peso_maximo
        self.objetos = []
        self.cadena = None  # Primer manejador

    def pesoTotal(self):
        return sum(obj.devPeso() for obj in self.objetos)

    def agregar(self, obj):
        if self.pesoTotal() + obj.devPeso() <= self.peso_maximo:
            self.objetos.append(obj)
            print(f"Objeto {COLOR.BLANCO} {obj.nombre} {COLOR.FIN} añadido al inventario")

            if isinstance(obj, InventarioHandler):
                obj.siguiente = self.cadena
                self.cadena = obj
        else:
            print(f"No se puede añadir {obj.nombre} al inventario. Peso máximo: {self.peso_maximo} ")

    def usar(self, personaje, nombre_obj):
        if self.cadena:
            self.cadena.manejar(personaje, nombre_obj, self)

    def tiene_objeto(self, tipo):
        return any(isinstance(obj, tipo) for obj in self.objetos)

    def eliminar(self, obj):
        if obj in self.objetos:
            self.objetos.remove(obj)
        else:
            for item in self.objetos:
                if isinstance(item, Bolsa) and obj in item.objetosBolsa:
                    item.objetosBolsa.remove(obj)
