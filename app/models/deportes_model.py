
class Deportes:

    def __init__(self):
        self.nombres = []

    def agregar_deportes(self, nombre_deporte):
        self.nombres.append(nombre_deporte)

    def obtener_lista(self):
        return [{"nombre": nombre} for nombre in self.nombres]
