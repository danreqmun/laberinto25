import json
from laberintoBuilder import LaberintoBuilder
from labBuilderImp import LabBuilderImp

class Director:
    def __init__(self):
        self.builder = None
        self.dict = None

    def obtenerJuego(self):
        return self.builder.obtenerJuego()

    def procesar(self, unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.fabricarObjetos()
        self.fabricarBichos()
        #self.NUEVOENTE()

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def iniBuilder(self):
        if self.dict['forma'] == 'cuadrado':
            self.builder=LaberintoBuilder()
        elif self.dict['forma'] == 'cuadrado_implementaciones':
            self.builder = LabBuilderImp()

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each, 'root')

        # recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0], each[1], each[2], each[3])


    def fabricarLaberintoRecursivo(self, each, padre):
        if each['tipo'] == 'habitacion':
            con = self.builder.fabricarHabitacion(each['num'])

            # Verifica si hay hijos tipo objeto
            if 'hijos' in each:
                for hijo in each['hijos']:
                    if 'objeto' in hijo:
                        if hijo['objeto'] == 'Totem':
                            totem = self.builder.fabricarTotem()
                            con.agregarHijo(totem)
                        elif hijo['objeto'] == 'Bolsa':
                            bolsa = self.builder.fabricarBolsa()
                            con.agregarHijo(bolsa)
            #if padre:
            #    padre.agregarHijo(con)

        elif each['tipo'] == 'tunel':
            self.builder.fabricarTunelEn(padre)

        # Recorre hijos recursivos si existen
        if 'hijos' in each:
            for hijo in each['hijos']:
                # Solo recursión si no es objeto
                if 'tipo' in hijo:
                    self.fabricarLaberintoRecursivo(hijo, con)

    def fabricarObjetos(self):
        for hab in self.dict['laberinto']:
            num = hab["num"]
            hijos = hab.get("hijos", [])
            for hijo in hijos:
                if hijo == "Totem":
                    self.builder.fabricarTotem()
                if hijo == "Pocima":
                    self.builder.fabricarPocima(num)
                if hijo == "Bolsa":
                    self.builder.fabricarBolsa(num)

    def leerArchivo(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict = data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def fabricarBichos(self):
        for each in self.dict['bichos']:
            self.builder.fabricarBicho(each['modo'], each['posicion'])