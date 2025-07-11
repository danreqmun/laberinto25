from color import COLOR

class EstadoEnte:
    def __init__(self):
        pass

    def vivir(self, ente):
        pass

    def morir(self, ente):
        pass

class Vivo(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print(f"{COLOR.ORADOR} El ente está vivo {COLOR.FIN}")

    def morir(self, ente):
        print(f"{COLOR.ORADOR} El ente muere {COLOR.FIN}")
        ente.estadoEnte = Muerto()


class Muerto(EstadoEnte):
    def __init__(self):
        super().__init__()

    def vivir(self, ente):
        print(f"{COLOR.ORADOR} El ente ha revivido {COLOR.FIN}")
        ente.estadoEnte = Vivo()

    def morir(self, ente):
        print(f"{COLOR.ORADOR} El ente {ente} ya está muerto {COLOR.FIN}")
        ente.juego.terminarJuego()