from estadoEnte import Vivo, Muerto
from color import COLOR
from inventario import Inventario
from inventarioHandler import InventarioHandler
#from bicho import Bicho
from objetosMapa import ObjetosMapa
from totem import Totem
from pocima import Pocima
from bolsa import Bolsa
from monedaFactory import MonedaFactory
import random

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
        print(f"{COLOR.WARNINGACCION} Ataque {COLOR.FIN} : {COLOR.ALGOMALO} {self} está siendo atacado por {unAtacante} ({unAtacante.poder} poder){COLOR.FIN}")

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
                oro = MonedaFactory.getMoneda("oro")
                plata = MonedaFactory.getMoneda("plata")
                o, p = random.randint(1, 4), random.randint(3, 10)
                for _ in range(o):
                    unAtacante.posicion.agregarHijo(oro)  # La deja en la habitación
                for _ in range(p):
                    unAtacante.posicion.agregarHijo(plata)
                print(f"{COLOR.ORADOR} {self} ha soltado {COLOR.BLANCO} {o} monedas de oro y {p} monedas de plata al morir {COLOR.FIN}")

                for hijo in list(unAtacante.posicion.hijos):
                    # for hijo in alguien.posicion.hijos[:]:
                    from moneda import Moneda
                    if isinstance(hijo, Moneda):
                        hijo.recoger(unAtacante)
                        unAtacante.posicion.hijos.remove(hijo)

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