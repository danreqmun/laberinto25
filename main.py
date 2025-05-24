from Juego import *
from Implementaciones import *
from Juego import COLOR


fm = Creator()
juego = Juego()
juego.laberinto = juego.crearLaberinto4habitacionesImplementaciones(fm)


print("\n\nLaberinto 4 habitaciones IMPLEMENTACIONES\n")

for hab in juego.laberinto.hijos:
    print(f"Habitación: {hab.num}")

print()

for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} pts de vida y {bicho.poder} pts de poder")
    print(f"Posición (habitación) del bicho: {bicho.posicion.num}")
    print()

juego.iniciar_juego()
