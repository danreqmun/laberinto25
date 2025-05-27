from estadoEnte import Vivo, Muerto
from color import COLOR
#from inventario import Inventario
#from bicho import Bicho
from objetosMapa import ObjetosMapa, Bolsa
#from hojaObjetos import Totem, Pocima

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()

    def clonarLaberinto(self, tunel):
        pass


    """
    def esAtacadoPor(self, unAtacante):
        print(f"{COLOR.WARNINGACCION} Ataque {COLOR.FIN} : {self} está siendo atacado por {unAtacante}")
        self.vidas = self.vidas - unAtacante.poder

        if self.vidas < 0:
            self.vidas = 0

        print(f"{COLOR.ORADOR} {self} Vidas restantes: {self.vidas} {COLOR.FIN}")

        if self.vidas == 0 and isinstance(self, Personaje):
            print(f"{COLOR.ORADOR} El ente {self} ha muerto {COLOR.FIN}")
            if isinstance(self, Personaje):
                if self.inventario.tiene_objeto(Totem):
                    print(f"{COLOR.ORADOR} {self.nombre} ha usado el Tótem de la inmortalidad... {COLOR.BLANCO} ¡HA REVIVIDO! {COLOR.FIN}")
                    self.inventario.usar(self, "Tótem de la inmortalidad")
                    return
                else:
                    self.estadoEnte = Muerto()
                    time.sleep(2)
                    self.estadoEnte.morir(self)
        from bicho import Bicho
        if self.vidas == 0 and isinstance(self, Bicho):
            self.estadoEnte.morir(self)
    """

    def esAtacadoPor(self, unAtacante):
        print(f"{COLOR.WARNINGACCION} Ataque {COLOR.FIN} : {self} está siendo atacado por {unAtacante}")
        self.vidas = self.vidas - unAtacante.poder
        if self.vidas < 0:
            self.vidas = 0
        print("Vidas restantes: ", self.vidas)
        if self.vidas == 0:
            from bicho import Bicho
            if isinstance(self, Bicho):
                self.juego.terminarBicho(self)
                #self.juego.bichos.remove(self)
            self.estadoEnte.morir(self)

class Personaje(Ente):
    def __init__(self, vidas, poder, posicion, juego, nombre):
        super().__init__()
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.juego = juego
        self.nombre = nombre

        #self.inventario = Inventario(peso_maximo=10)     # IMPLEMENTACION

    def clonarLaberinto(self, tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()

    def caminar(self):
        #print(self.posicion.num)
        self.posicion.caminarAleatorio(self)
        print(f"El personaje {self} está caminando \n")

    def estaVivo(self):
        return self.vidas > 0

    def __repr__(self):
        return self.nombre