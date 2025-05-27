from color import COLOR
from director import Director

import time
import os
import signal

def actualizar(juego):
    while len(juego.bichos) > 0 and juego.personaje.vidas>0:
        #juego.personaje.caminar()
        #if juego.personaje.vidas>0:
        print("posicion de Paco",juego.personaje.posicion.num)
        juego.personaje.caminar()
        juego.buscarBicho()
        time.sleep(3)
        print(f"\n\n {COLOR.ALGOMALO}{juego.bichos} \n\n\n {juego.bichos_threads} {COLOR.FIN}\n\n\n")

    juego.terminarJuego()
    os.kill(os.getpid(),signal.SIGTERM)

director = Director()
#ruta = './lab4habImplementaciones.json'
ruta = './lab4hab.json'

datos = director.leerArchivo(ruta)
if datos:
    print("Datos del JSON: ")
    print(datos)
else:
    print("Error al cargar el JSON")

juego = director.procesar(ruta)
juego = director.obtenerJuego()
juego.agregarPersonaje("Paco")



'''
# Mostrar los bichos del juego y atacar
for bicho in juego.bichos:
    print(bicho)
    print(f"Bicho con {bicho.vidas} vidas y {bicho.poder} de poder")
    print(f"Posición {bicho.posicion.num}")
    #juego.buscarPersonaje(bicho)  # Invoca el ataque si el bicho está en la misma posición que el personaje
    #juego.buscarBicho(bicho)
# Mostrar los fantasmas y sus atributos
'''

'''
for fantasma in juego.fantasmas:
    print(fantasma)
    print(f"Fantasma con {fantasma.vidas} vidas y {fantasma.poderMagico} de poderMagico")
    print(f"Posición {fantasma.posicion.num}")
    juego.buscarPersonajeParaSupportear(fantasma)
'''


# Mostrar el personaje y sus atributos
# print("Personaje", juego.personaje.nombre, juego.personaje.vidas,juego.personaje.posicion.num)
#juego.buscarBicho()

# Lógica de abrir puertas, lanzar bichos y terminar bichos
juego.abrirPuertas()
print(f"Posición personaje tras caminar: {juego.personaje.posicion.num}")
juego.lanzarBichos()
actualizar(juego)