class Candidatos:

    def __init__(self):
        self.data = []
        self.cantidad_total = None

    def agregar_candidatos(self, nombres, total):
        self.data.append({
            "candidato_nombre": nombres
        })
        self.cantidad_total = int(total)

    def obtener_lista(self):
        return {
            "data": self.data,
            "total_candidatos": int(self.cantidad_total)
        }
