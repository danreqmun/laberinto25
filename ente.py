from estadoEnte import Vivo, Muerto
from color import COLOR
from inventario import Inventario
from inventarioHandler import InventarioHandler
#from bicho import Bicho
from objetosMapa import ObjetosMapa
from totem import Totem
from pocima import Pocima
from bolsa import Bolsa


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


    def esAtacadoPor(self, unAtacante):
        print(f"{COLOR.WARNINGACCION} Ataque {COLOR.FIN} : {self} está siendo atacado por {unAtacante} ({unAtacante.poder} poder)")
        self.vidas = self.vidas - unAtacante.poder
        if self.vidas < 0:
            self.vidas = 0
        print("Vidas restantes: ", self.vidas)
        if self.vidas == 0:
            if isinstance(self, Personaje):
                if self.inventario.tiene_objeto(Totem):
                    self.inventario.usar(self, "Tótem de la inmortalidad")
                    return

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

        self.inventario = Inventario(peso_maximo=10)     # IMPLEMENTACION

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