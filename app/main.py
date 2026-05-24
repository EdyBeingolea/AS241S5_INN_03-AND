from fastapi import FastAPI

from app.core.deportes_rest import app as deportes_app
from app.core.candidato_rest import app as candidato_app
import uvicorn


app = FastAPI()
app.include_router(deportes_app.router)
app.include_router(candidato_app.router)


def main():
    print("🚀 API iniciada en http://127.0.0.1:8000")

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()