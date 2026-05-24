from fastapi import FastAPI
import app.services.deportes_service as service

app = FastAPI()

@app.get("/lista-deportes")
def lista_deportes():
    return service.lista_deporte()

