from app.models.candidatos_model import CandidatoLista
from app.models.deportes_model import Deportes
import pandas as pd
import numpy as np

ruta_data = "https://docs.google.com/spreadsheets/d/1FuZV6MM_B1O50IbZig92IBkCk44jU3Dnx6vF42OgaRA/export?format=csv&gid=210583738"

data_frame = pd.read_csv(ruta_data)

nombres_deporte = data_frame['DISCIPLINA DEPORTIVA'].value_counts()


def lista_nombres_deporte():

    deportes = Deportes()
    total_registros = np.sum(nombres_deporte)

    for nombre, cantidad in nombres_deporte.items():
        deportes.agregar_deporte(nombre, int(cantidad), total_registros)

    return deportes.obtener_lista()


def lista_candidatos_deporte(deporte: str):

    candidatos = CandidatoLista()
    deporte_escojido = data_frame.query(
         "`DISCIPLINA DEPORTIVA` == @deporte"
    )

    nombres_candidatos = deporte_escojido[
        'NOMBRE DEL DEPORTISTA'
    ].value_counts()

    total_candidatos = np.sum(nombres_candidatos)

    for nombre in nombres_candidatos.index:
        candidatos.agregar_candidatos(nombre, int(total_candidatos))

    return candidatos.obtener_lista()


