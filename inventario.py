from color import COLOR

class Inventario:
    def __init__(self, peso_maximo):
        self.peso_maximo = peso_maximo
        self.objetos = []

    def pesoTotal(self):
        return sum(obj.devPeso() for obj in self.objetos)

    def agregar(self, obj):
        if self.pesoTotal() + obj.devPeso() <= self.peso_maximo:
            self.objetos.append(obj)
            print(f"Objeto {COLOR.BLANCO} {obj.nombre} {COLOR.FIN} añadido al inventario")
        else:
            print(f"No se puede añadir {obj.nombre} al inventario. Peso máximo: {self.peso_maximo} ")

    def usar(self, personaje, nombre_obj):
        for obj in self.objetos:
            if obj.nombre == nombre_obj:
                obj.usar(personaje)
                self.objetos.remove(obj)
                break
            else:
                print(f"No tienes el objeto {obj.nombre}")

    def tiene_objeto(self, tipo):
        return any(isinstance(obj, tipo) for obj in self.objetos)