from pathlib import Path
import sys
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.deportes_model import Deportes

ruta_data =  r"data/processed/decan_0.csv"

data_frame = pd.read_csv(ruta_data, encoding="latin1", sep=";" )

nombres_deporte = data_frame['DISCIPLINA DEPORTIVA'].unique()

def lista_nombres_deporte():

    deportes = Deportes()
    for valor in nombres_deporte:
        deportes.agregar_deportes(valor)
    return deportes.obtener_lista()

