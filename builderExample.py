from bolsa import Bolsa
from color import COLOR
from director import Director

import time
import os
import signal

def actualizar(juego):
    while len(juego.bichos) > 0 and juego.personaje.vidas>0:
        print(f"posicion de {juego.personaje.nombre}: {juego.personaje.posicion}")
        juego.personaje.caminar()
        juego.buscarBicho()
        time.sleep(3)
        print(f"\n\n {COLOR.ALGOMALO}{juego.bichos} \n {juego.bichos_threads} {COLOR.FIN}\n\n")

        juego.personaje.inventario.imprimir(juego.personaje)

    juego.terminarJuego()
    os.kill(os.getpid(),signal.SIGTERM)

director = Director()
ruta = './lab4habImplementaciones.json'
#ruta = './lab4hab.json'

datos = director.leerArchivo(ruta)
if datos:
    print("Datos del JSON: ")
    print(datos)
else:
    print("Error al cargar el JSON")

juego = director.procesar(ruta)
juego = director.obtenerJuego()
juego.agregarPersonaje("Paco")



juego.abrirPuertas()
print(f"Posición personaje tras caminar: {juego.personaje.posicion.num}")
juego.lanzarBichos()
actualizar(juego)