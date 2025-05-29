class InventarioHandler:
    def __init__(self):
        self.siguiente = None

    def manejar(self, personaje, nombre_obj, inventario):
        if self.siguiente:
            return self.siguiente.manejar(personaje, nombre_obj, inventario)
        print(f"No tienes el objeto {nombre_obj}")
        return False