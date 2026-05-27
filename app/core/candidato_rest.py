from fastapi import FastAPI
import app.services.candidato_service as service

app = FastAPI()


@app.get("/candidato/lista")
def lista_candidato():
    return service.lista_candidato()


@app.get("/candidato/{candidato}")
def busqueda_candidato(candidato:str):
    return service.busqueda_candidato(candidato)