from moneda import Moneda

class MonedaFactory:
    _monedas = {}

    @staticmethod
    def getMoneda(tipo):
        if tipo not in MonedaFactory._monedas:
            if tipo == "oro":
                MonedaFactory._monedas[tipo] = Moneda("oro", 0.25)
            elif tipo == "plata":
                MonedaFactory._monedas[tipo] = Moneda("plata", 0.1)
        return MonedaFactory._monedas[tipo]
