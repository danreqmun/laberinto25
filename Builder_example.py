from Juego import *
from LabBuilder import *

def actualizar(juego):
    while len(juego.bichos) > 0:
        juego.personaje.caminar()
        juego.buscarBicho()
        time.sleep(5)
    print("ganó el personaje")

director = Director()
ruta = './lab4habImplementaciones.json'

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