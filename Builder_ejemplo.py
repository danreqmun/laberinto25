import time

import Juego
from Juego import *

if __name__ == "__main__":

    def update(juego):
        while len(juego.bichos) > 0:
            juego.personaje.caminar()
            juego.buscarBicho()
            time.sleep(15)
        print(f"GANÓ EL PERSONAJE {juego.personaje.nombre}")

    director = Director()

    ruta = "C:/Users/Dani/Desktop/Clase/3º/2do cuatrimestre/Diseño/json/lab4Hab.json"

    datos = director.leerArchivo(ruta)
    if datos:
        print("Datos del JSON:")
        print(datos)
    else:
        print("No hay datos. ERROR.")

    juego = director.procesar(ruta)
    juego = director.obtenerJuego()
    juego.agregarPersonaje("Telmar")

    juego.abrirPuertas()
    print(f"Posición del personaje después de caminar: {juego.personaje.posicion.num}")
    juego.lanzarBichos()
    update(juego)