class CandidatoLista:

    def __init__(self):
        self.data = []
        self.candidato = None
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

    def obtener_candidato(self, candidato):
        self.candidato = candidato

    def devolver_canidato(self):
        return {
            "candidato": self.candidato
        }


class Candidato:
    def __init__(self):
        self.lista_candidato = []
        self.cantidad_total = 0

    def agregar_lista_candidato(self, item, fecha_corte, deportista, deporte, resolucion, estado, fecha_registro, observacion, cantidad_total):
        self.lista_candidato.append({
            "item": item,
            "fecha_corte": fecha_corte,
            "deportista": deportista,
            "deporte": deporte,
            "resolucion": resolucion,
            "estado": estado,
            "fecha_registro": fecha_registro,
            "observacion": observacion,
        })

        self.cantidad_total = cantidad_total

    def devolver_lista_candiato(self):
        return {
            "data": self.lista_candidato,
            "cantidad_total" : self.cantidad_total
        }
