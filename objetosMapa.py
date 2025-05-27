class ObjetosMapa:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self, personaje):
        pass

    def recoger(self, personaje):
        pass

    def devPeso(self):
        pass

    def recorrer(self, func):
        pass

class Bolsa(ObjetosMapa):
    def __init__(self, nombre = "Bolsa"):
        super().__init__(nombre)
        self.hijos = []

    def agregar(self, obj):
        if isinstance(obj, ObjetosMapa):
            self.hijos.append(obj)
        else:
            print(f"Esto no es un objeto del mapa")

    def recoger(self, personaje):
        from ente import Personaje
        if isinstance(personaje, Personaje):
            personaje.inventario.agregar(self)

    def usar(self, personaje):
        print(f"Usando el contenido de la bolsa '{self.nombre}':")
        for obj in self.hijos:
            obj.usar(personaje)

    def devPeso(self):
        return sum(obj.devPeso() for obj in self.hijos)