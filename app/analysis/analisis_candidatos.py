from app.models.candidatos_model import Candidatos

import pandas as pd
import numpy as np

ruta_data = "https://docs.google.com/spreadsheets/d/1FuZV6MM_B1O50IbZig92IBkCk44jU3Dnx6vF42OgaRA/export?format=csv&gid=210583738"

data_frame = pd.read_csv(ruta_data)

def busqueda_candidato(nombre: str):

    candidato = Candidatos()

    nombre_busqueda = nombre.strip().upper()

    buscar_candidato = data_frame[
        data_frame["NOMBRE DEL DEPORTISTA"].str.upper().str.contains(nombre_busqueda, na=False, regex=False)
    ]

    if buscar_candidato.empty:
        return {
            "mensaje": "Candidato no encontrado"
        }

    nombre_candidato = buscar_candidato["NOMBRE DEL DEPORTISTA"].tolist()
    
    candidato.obtener_candidato(nombre_candidato)

    return candidato.devolver_canidato()


