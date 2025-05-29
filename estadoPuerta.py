from color import COLOR

class EstadoPuerta:
    def __init__(self):
        pass

    def abrir(self, puerta):
        pass

    def cerrar(self, puerta):
        pass

    def entrar(self, puerta, alguien):
        pass

class Abierta(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print(f"{COLOR.ORADOR} La puerta ya está abierta {COLOR.FIN}")

    def cerrar(self, puerta):
        print(f"{COLOR.ORADOR} Cerrando la puerta {COLOR.FIN}")
        puerta.estadoPuerta = Cerrada()

    def entrar(self, puerta, alguien):
        puerta.puedeEntrar(alguien)

class Cerrada(EstadoPuerta):
    def __init__(self):
        super().__init__()

    def abrir(self, puerta):
        print(f"{COLOR.ORADOR} Abriendo la puerta {COLOR.FIN}")
        puerta.estadoPuerta = Abierta()

    def cerrar(self, puerta):
        print(f"{COLOR.ORADOR} La puerta ya está cerrada {COLOR.FIN}")

    def entrar(self, puerta, alguien):
        pass