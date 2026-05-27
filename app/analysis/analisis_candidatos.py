from app.models.candidatos_model import CandidatoLista, Candidato

import pandas as pd
import numpy as np

ruta_data = "https://docs.google.com/spreadsheets/d/1FuZV6MM_B1O50IbZig92IBkCk44jU3Dnx6vF42OgaRA/export?format=csv&gid=210583738"

data_frame = pd.read_csv(ruta_data)


def busqueda_candidato(nombre: str):

    candidato_lista = CandidatoLista()

    nombre_busqueda = nombre.strip().upper()

    buscar_candidato = data_frame[
        data_frame["NOMBRE DEL DEPORTISTA"].str.upper().str.contains(
            nombre_busqueda, na=False, regex=False)
    ]

    if buscar_candidato.empty:
        return {
            "mensaje": "Candidato no encontrado"
        }

    nombre_candidato = buscar_candidato["NOMBRE DEL DEPORTISTA"].tolist()

    candidato_lista.obtener_candidato(nombre_candidato)

    return candidato_lista.devolver_canidato()


def lista_candidatos():

    candito = Candidato()

    cantidad_total = len(data_frame)

    for _, fila in data_frame.iterrows():

        observacion = fila["OBSERVACIONES"]

        # validar NaN
        if pd.isna(observacion):
            observacion = None

        candito.agregar_lista_candidato(
            item=fila["ITEM"],
            fecha_corte=str(fila["FECHA_CORTE"]),
            deportista=fila["NOMBRE DEL DEPORTISTA"],
            deporte=fila["DISCIPLINA DEPORTIVA"],
            resolucion=fila["N° DE RESOLUCION"],
            estado=fila["ESTADO"],
            fecha_registro=str(fila["FECHA DE REGISTRO"]),
            observacion=observacion,
            cantidad_total=cantidad_total
        )

    return candito.devolver_lista_candiato()



