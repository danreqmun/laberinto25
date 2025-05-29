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

        #para imprimir el inventario por cada loop
        print(f"\n{COLOR.MORADO} 🧾 Inventario de {juego.personaje.nombre} {COLOR.FIN}")
        for obj in juego.personaje.inventario.objetos:
            if isinstance(obj, Bolsa):
                print(f" - Bolsa con {len(obj.objetosBolsa)} objetos:")
                for sub in obj.objetosBolsa:
                    print(f"    • {sub.nombre} (peso: {sub.devPeso()})")
            else:
                print(f" - {obj.nombre} (peso: {obj.devPeso()})")

        print(f"\nPeso total: {juego.personaje.inventario.pesoTotal()} / {juego.personaje.inventario.peso_maximo}\n")

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