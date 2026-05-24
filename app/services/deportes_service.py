import app.analysis.analisis_deportes as analisis


def lista_deporte():
    return analisis.lista_nombres_deporte()


def lista_candidatos_deporte(deporte: str):
    return analisis.lista_candidatos_deporte(deporte)
