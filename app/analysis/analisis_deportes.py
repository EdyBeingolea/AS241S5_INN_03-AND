from app.models.candidatos_model import Candidatos
from app.models.deportes_model import Deportes
from pathlib import Path
import sys
import pandas as pd
import numpy as np
sys.path.append(str(Path(__file__).resolve().parents[2]))


ruta_data = r"data/processed/decan_0.csv"

data_frame = pd.read_csv(ruta_data, encoding="latin1", sep=";")

nombres_deporte = data_frame['DISCIPLINA DEPORTIVA'].value_counts()


def lista_nombres_deporte():

    deportes = Deportes()
    total_registros = np.sum(nombres_deporte)

    for nombre, cantidad in nombres_deporte.items():
        deportes.agregar_deporte(nombre, int(cantidad), total_registros)

    return deportes.obtener_lista()


def lista_candidatos_deporte(deporte: str):

    candidatos = Candidatos()
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
