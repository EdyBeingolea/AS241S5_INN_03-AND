from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.deportes_rest import app as deportes_app
from app.core.candidato_rest import app as candidato_app
import uvicorn
import os


app = FastAPI()
app.include_router(deportes_app.router)
app.include_router(candidato_app.router)

default_origins = ["http://localhost:5173"]
allow_all = os.environ.get("ALLOW_ALL_ORIGINS", "0") in ("1", "true", "True")
origins = ["*"] if allow_all else default_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))

    print(f"🚀 API iniciada en http://{host}:{port}")

    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=True,
    )


if __name__ == "__main__":
    main()
