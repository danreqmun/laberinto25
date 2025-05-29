from objetosMapa import ObjetosMapa

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