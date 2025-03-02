
""" 2/03/25 """

# FACTORY METHOD
class ElementoMapa:
    def __init__(self):
        pass

    def entrar(self):
        pass

class Habitacion(ElementoMapa):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def entrar(self):
        print(f"entrando en la habitación {self.num}")

    def __repr__(self):
        return f" habitación {self.num}"
        #para que a la salida por consola no imprima la dir de memoria


class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self):
        print("te has chocado contra una pared")

    def __repr__(self):
        return "Pared"

class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        print("te has chocado contra una pared bomba")

    def is_activa(self):
        if self.activa:
            return "Hmm, parece una pared normal y corriente... espero que no... explote..."
        else:
            return "Creo que es una pared... normal... como las demás..."

    def activar_pared_bomba(self):
        self.activa = True

    def __repr__(self):
        return "Pared bomba"


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    def entrar(self):
        if self.abierta:
            print(f"puerta {self.lado1.num} - {self.lado2.num} está abierta, paso")
        else:
            print(f"puerta  {self.lado1.num} - {self.lado2.num} está cerrada, no puedo pasar")

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False

    def __repr__(self):
        if self.abierta:
            return "Puerta abierta"
        else:
            return "Puerta cerrada"


class Laberinto(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.habitaciones = []

    def entrar(self):
        print("Bienenido al laberinto")

    def agregar_habitacion(self, hab):
        self.habitaciones.append(hab)

    def eliminar_habitacion(self, hab):
        if hab in self.habitaciones:
            self.habitaciones.remove(hab)
        else:
            print("no existe tal habitación")

    def obtener_habitacion(self, num):
        for hab in self.habitaciones:
            if hab.num == num:
                return hab
        return None


# DECORATOR (Bomba en Pared)
class Decorator(ElementoMapa):
    def __init__(self, elemento):
        self.elemento = elemento


class Bomba(Decorator):
    def __init__(self, elemento):
        super().__init__(elemento)
        self.activa = False

    def __repr__(self):
        return "Bomba"



# CREATOR
class Creator:
    def fabricar_laberinto(self):
        return Laberinto()

    def fabricar_pared(self):
        return Pared()

    def fabricar_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)

    def fabricar_habitacion(self, num):
        habitacion = Habitacion(num)
        habitacion.norte = self.fabricar_pared()
        habitacion.sur = self.fabricar_pared()
        habitacion.este = self.fabricar_pared()
        habitacion.oeste = self.fabricar_pared()
        return habitacion

    def fabricar_bomba(self, elemento):
        return Bomba(elemento)

    def fabricar_bicho(self, vidas, poder, modo, posicion):
        return Bicho(vidas, poder, modo, posicion)

    def fabricar_bicho_agresivo(self):
        return Agresivo()

    def fabricar_bicho_perezoso(self):
        return Perezoso()


class CreatorB(Creator):
    def fabricar_pared_bomba(self):
        return ParedBomba()


# Modo de Bichos (Strategy)
class Modo:
    def actuar(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def actuar(self):
        print("El bicho ataca agresivamente")

    def __repr__(self):
        return "agresivo"

class Perezoso(Modo):
    def __init__(self):
        super().__init__()

    def actuar(self):
        print("El bicho se mueve lentamente...")

    def __repr__(self):
        return "perezoso"

class Bicho:
    def __init__(self, vidas, poder, modo, posicion):
        self.vidas = vidas
        self.poder = poder
        self.modo = modo
        self.posicion = posicion

    def actuar(self):
        self.modo.actuar()

    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 5

    def iniPerezoso(self):
        self.modo = Perezoso()
        self.poder = 1
        self.vidas = 5

    def __str__(self):
        return f"Bicho --- vidas: {self.vidas}, Poder: {self.poder}, Posicion: {self.posicion}, Modo: {self.modo}"

    def __repr__(self):
        return "Bicho -- vidas: {}, Poder: {}, Posicion: {}, Modo: {}".format(self.vidas, self.poder, self.posicion, self.modo)



# JUEGO
class Juego:
    def __init__(self):
        self.laberinto = Laberinto()
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    def obtenerHabitacion(self, num):
        return self.laberinto.obtener_habitacion(num)


    def crearLaberinto4habitaciones(self, creator):
        #   hab1  hab2
        #   hab3  hab4
        laberinto = creator.fabricar_laberinto()

        hab1 = creator.fabricar_habitacion(1)
        hab2 = creator.fabricar_habitacion(2)
        hab3 = creator.fabricar_habitacion(3)
        hab4 = creator.fabricar_habitacion(4)

        puerta12 = creator.fabricar_puerta(hab1, hab2)
        puerta24 = creator.fabricar_puerta(hab2, hab4)
        puerta43 = creator.fabricar_puerta(hab4, hab3)
        puerta31 = creator.fabricar_puerta(hab3, hab1)

        hab1.este = puerta12
        hab2.sur = puerta24
        hab3.norte = puerta31
        hab4.oeste = puerta43

        hab1.sur = puerta31
        hab2.oeste = puerta12
        hab3.este = puerta43
        hab4.norte = puerta24

        bicho1 = creator.fabricar_bicho(5, 10, creator.fabricar_bicho_agresivo(), hab1)
        self.agregar_bicho(bicho1)
        bicho3 = creator.fabricar_bicho(5, 10, creator.fabricar_bicho_agresivo(), hab3)
        self.agregar_bicho(bicho3)
        bicho2 = creator.fabricar_bicho(5, 1, creator.fabricar_bicho_perezoso(), hab2)
        self.agregar_bicho(bicho2)
        bicho4 = creator.fabricar_bicho(5, 1, creator.fabricar_bicho_perezoso(), hab4)
        self.agregar_bicho(bicho4)

        hab1.bicho = bicho1
        hab2.bicho = bicho2
        hab3.bicho = bicho3
        hab4.bicho = bicho4

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        laberinto.agregar_habitacion(hab3)
        laberinto.agregar_habitacion(hab4)

        return laberinto

    def crearLaberinto2HabFM(self, creator):
        laberinto = creator.fabricar_laberinto()

        hab1 = creator.fabricar_habitacion(1)
        hab2 = creator.fabricar_habitacion(2)

        puerta12 = creator.fabricar_puerta(hab1, hab2)

        hab1.este = puerta12
        hab2.oeste = puerta12

        hab1.oeste = creator.fabricar_pared_bomba()
        hab2.este = creator.fabricar_pared_bomba()

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)

        return laberinto

    def crearLaberinto2HabBomba(self, creator):
        laberinto = creator.fabricar_laberinto()
        hab1 = creator.fabricar_habitacion(1)
        hab2 = creator.fabricar_habitacion(2)
        puerta = creator.fabricar_puerta(hab1, hab2)

        hab1.sur = puerta
        hab2.norte = puerta

        pared1 = creator.fabricar_pared()
        bomba1 = creator.fabricar_bomba(pared1)
        hab1.este = bomba1

        pared2 = creator.fabricar_pared()
        bomba2 = creator.fabricar_bomba(pared2)
        hab2.oeste = bomba2

        laberinto.agregar_habitacion(hab1)
        laberinto.agregar_habitacion(hab2)
        return laberinto



if __name__ == "__main__":
    print("Laberinto 4 habitaciones con bichos\n")

    fm = Creator()
    juego = Juego()
    juego.laberinto = juego.crearLaberinto4habitaciones(fm)
    hab1 = juego.obtenerHabitacion(1)
    hab2 = juego.obtenerHabitacion(2)
    hab3 = juego.obtenerHabitacion(3)
    hab4 = juego.obtenerHabitacion(4)

    for hab in juego.laberinto.habitaciones:
        print(f"Habitación: {hab.num}")
        if hasattr(hab, "bicho"):
            bicho = hab.bicho
            print(f"Bicho --- vidas: {bicho.vidas}, Poder: {bicho.poder}, Posicion: {bicho.posicion}, Modo: {bicho.modo}")

        print(hab.norte)


        print("\n")

    print("\n\nLaberinto 2 habitaciones con pared bomba\n")

    fmb = CreatorB()
    juego.laberinto = juego.crearLaberinto2HabFM(fmb)
    hab1 = juego.obtenerHabitacion(1)
    hab2 = juego.obtenerHabitacion(2)

    print(f"Hab {hab1.num} - este: {hab1.este}")
    print(f"Hab {hab1.num} - oeste: {hab1.oeste.is_activa()} (activa: {hab1.oeste.activa})")
    hab1.este.entrar()
    print("Se me ha olvidado que las puertas se tienen que abrir para pasar primero")
    hab1.este.abrir()
    hab1.este.entrar()
    hab2.este.activar_pared_bomba()
    print(f"Hab {hab2.num} - este: {hab2.este.is_activa()} (activa: {hab2.este.activa})")
    print()
    for hab in juego.laberinto.habitaciones:
        print(f"Habitacion: {hab.num}")
        print(f"Norte: {hab.norte}, Sur: {hab.sur}, Este: {hab.este}, Oeste: {hab.oeste}")

    print("\n\nLaberinto 2 habitaciones con bombas")

    fm = Creator()
    juego = Juego()
    juego.laberinto = juego.crearLaberinto2HabBomba(fm)
    hab1 = juego.obtenerHabitacion(1)
    hab2 = juego.obtenerHabitacion(2)

    for hab in juego.laberinto.habitaciones:
        print(f"Habitacion: {hab.num}")
        print(f"Norte: {hab.norte}, Sur: {hab.sur}, Este: {hab.este}, Oeste: {hab.oeste}")
