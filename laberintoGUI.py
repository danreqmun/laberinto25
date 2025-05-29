from point import Point
from director import Director
import tkinter as tk

class LaberintoGUI:
    def __init__(self, master, laberinto_file):
        self.master = master
        self.laberinto_file = laberinto_file
        self.juego = None
        self.canvas = None
        self.ancho = 0
        self.alto = 0

        self.load_laberinto()
        self.init_ui()

    def load_laberinto(self):
        director = Director()
        director.procesar(self.laberinto_file)
        self.juego = director.obtenerJuego()
        self.juego.agregarPersonaje("Paco")

        self.personaje = self.juego.personaje #guardar personaje
        self.bichos = self.juego.bichos

        for bicho in self.bichos:
            if isinstance(bicho.posicion, int):
                bicho.posicion = self.juego.obtenerHabitacion(bicho.posicion)

        print(f"Bichos cargados: {self.bichos}")

    def init_ui(self):
        self.master.title("El Laberinto")
        self.canvas = tk.Canvas(self.master, width=1280, height=720, bg = "white")
        self.canvas.pack()

        self.calcularLaberinto()
        for hab in self.juego.laberinto.objetosBolsa:
            print("num-punto", hab.num, hab.forma.punto.x, hab.forma.punto.y)
        self.dibujarLaberinto()
        self.dibujarPersonaje()
        self.dibujarBichos()

    def dibujarPersonaje(self):
        hab = self.personaje.posicion
        print(f"Posición personaje: {self.personaje.posicion}")
        print(f"personaje posicion num {self.personaje.posicion.num}")
        print("forma x personaje", hab.forma.punto.x)
        x = hab.forma.punto.x + hab.forma.extent.x // 2
        y = hab.forma.punto.y + hab.forma.extent.y // 2

        radio = 10
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue", outline="black")
        self.canvas.create_text(x, y - 15, text=self.personaje.nombre, fill="black", font=("Arial", 8))

    def dibujarBichos(self):
        colores = ["red", "green", "orange", "purple"]
        for idx, bicho in enumerate(self.bichos):
            # Resuelve la habitación a partir del número de la posición del bicho
            pos = bicho.posicion  # Aquí ya se debe tener la habitación correcta con las coordenadas transformadas
            hab = juego.obtenerHabitacion(pos)
            print("bicho posicion", bicho.posicion)
            print("bicho posicion num:", hab.num)
            print("forma x bicho:", hab.forma.punto.x)
            print("forma y bicho:", hab.forma.punto.y)

            x = hab.forma.punto.x + hab.forma.extent.x // 2
            y = hab.forma.punto.y + hab.forma.extent.y // 2

            offset = 15 * (idx % 4)  # Pequeño desplazamiento para evitar superposición
            radio = 8
            self.canvas.create_oval(x - radio + offset, y - radio + offset, x + radio + offset, y + radio + offset,
                                    fill=colores[idx % len(colores)], outline="black")
            self.canvas.create_text(x + offset, y + offset + 10, text=f"B{idx + 1}", fill="black", font=("Arial", 7))

    def calcularLaberinto(self):
        self.calcularPosicion()
        self.normalizar()
        self.calcularTamContenedor()
        self.asignarPuntosReales()

    def dibujarLaberinto(self):
        self.juego.laberinto.aceptar(self)

    def visitarHabitacion(self, hab):
        self.dibujarRectangulo(hab.forma)

    def visitarPared(self, pared):
        pass
    def visitarPuerta(self, puerta):
        pass
    def visitarBomba(self, bomba):
        pass
    def visitarTunel(self, tunel):
        pass

    def dibujarRectangulo(self, forma):
        self.canvas.create_rectangle(forma.punto.x, forma.punto.y, forma.punto.x + forma.extent.x,
                                     forma.punto.y + forma.extent.y, fill="lightgray")

    def calcularPosicion(self):
        habitacion1 = self.juego.obtenerHabitacion(1)
        habitacion1.forma.punto = Point(0, 0)
        for habitacion in self.juego.laberinto.objetosBolsa:
            habitacion.calcularPosicion()

    def normalizar(self):
        min_x = 0
        min_y = 0

        # Buscar min_x y min_y
        for each in self.juego.laberinto.objetosBolsa:
            min_x = min(min_x, each.forma.punto.x)
            min_y = min(min_y, each.forma.punto.y)

        # Ajustar puntos
        for each in self.juego.laberinto.objetosBolsa:
            un_punto = each.forma.punto
            nuevo_x = un_punto.x + abs(min_x)
            nuevo_y = un_punto.y + abs(min_y)
            each.forma.punto = Point(nuevo_x, nuevo_y)

    def calcularTamContenedor(self):
        max_x = 0
        max_y = 0

        for each in self.juego.laberinto.objetosBolsa:
            max_x = max(max_x, each.forma.punto.x)
            max_y = max(max_y, each.forma.punto.y)

        max_x += 1
        max_y += 1

        self.ancho = round(1050 / max_x)
        self.alto = round(600 / max_y)

    def asignarPuntosReales(self):
        origen_x, origen_y = 70, 10

        for each in self.juego.laberinto.objetosBolsa:
            x = origen_x + (each.forma.punto.x * self.ancho)
            y = origen_y + (each.forma.punto.y * self.alto)

            each.forma.punto = Point(x, y)  # Asumo que Punto(x, y) es una clase
            each.forma.extent = Point(self.ancho, self.alto)

if __name__ == '__main__':
    root = tk.Tk()
    gui = LaberintoGUI(root, "./lab4habImplementaciones.json")  # Use a default laberinto file
    root.mainloop()