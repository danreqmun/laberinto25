from hoja import Hoja

# DECORATOR
class Decorator(Hoja):
    def __init__(self, elemento):
        super().__init__()
        self.elemento = elemento