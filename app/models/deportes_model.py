class Deportes:

    def __init__(self):
        self._data = []
        self._total_personas = None

    def agregar_deporte(self, nombre, cantidad, cantidad_total):
        self._data.append({
            "nombre": str(nombre),
            "cantidad": int(cantidad)
        })
        self._total_personas = int(cantidad_total)

    def obtener_lista(self):
        return {
            "data": self._data,
            "total_personas": int(self._total_personas)
        }
