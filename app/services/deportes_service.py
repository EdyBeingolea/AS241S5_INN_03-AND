import app.analysis.analisis_deportes as anlisis


def lista_deporte():
    return anlisis.lista_nombres_deporte()


def lista_candidatos_deporte(deporte: str):
    return anlisis.lista_candidatos_deporte(deporte)
