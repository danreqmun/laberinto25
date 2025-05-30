from bolsa import Bolsa
from color import COLOR
from inventarioHandler import InventarioHandler
from moneda import Moneda
from objetosMapa import ObjetosMapa


class Inventario:
    def __init__(self, peso_maximo):
        self.peso_maximo = peso_maximo
        self.objetos = []
        self.cadena = None  # Primer manejador

    def pesoTotal(self):
        return sum(obj.devPeso() for obj in self.objetos)

    def agregar(self, obj):
        if self.pesoTotal() + obj.devPeso() <= self.peso_maximo:
            self.objetos.append(obj)
            if isinstance(obj, ObjetosMapa): print(f"Objeto {COLOR.BLANCO} {obj.nombre} {COLOR.FIN} añadido al inventario")
            if isinstance(obj, Moneda): print(f"Objeto {COLOR.BLANCO} moneda de {obj.tipo} {COLOR.FIN} añadido al inventario")

            if isinstance(obj, InventarioHandler):
                obj.siguiente = self.cadena
                self.cadena = obj
        else:
            print(f"No se puede añadir {obj.nombre} al inventario. Peso máximo: {self.peso_maximo} ")

    def usar(self, personaje, nombre_obj):
        if self.cadena:
            self.cadena.manejar(personaje, nombre_obj, self)

    def tiene_objeto(self, tipo):
        return any(isinstance(obj, tipo) for obj in self.objetos)

    def eliminar(self, obj):
        if obj in self.objetos:
            self.objetos.remove(obj)
        else:
            for item in self.objetos:
                if isinstance(item, Bolsa) and obj in item.objetosBolsa:
                    item.objetosBolsa.remove(obj)

    def imprimir(self, personaje):
        oro, plata = 0, 0
        print(f"\n{COLOR.MORADO} 🧾 Inventario de {personaje.nombre} {COLOR.FIN}")
        for obj in personaje.inventario.objetos:
            if isinstance(obj, Bolsa):
                print(f" - Bolsa con {len(obj.objetosBolsa)} objetos:")
                for sub in obj.objetosBolsa:
                    print(f"    • {sub.nombre} (peso: {sub.devPeso()})")
            if isinstance(obj, Moneda):
                if obj.tipo == "oro":
                    oro += 1
                elif obj.tipo == "plata":
                    plata += 1
            if not isinstance(obj, Moneda) and not isinstance(obj, Bolsa):
                print(f" - {obj.nombre} (peso: {obj.devPeso()})")
        if oro > 0: print(f" - {oro} monedas de oro (peso: {oro * 0.25:.2f})")
        if plata > 0: print(f" - {plata} monedas de plata (peso: {plata * 0.1:.1f})")
        print(f"\nPeso total: {personaje.inventario.pesoTotal()} / {personaje.inventario.peso_maximo}")
        print(f"{COLOR.MORADO} 🧾 Inventario de {personaje.nombre} {COLOR.FIN}\n\n")
