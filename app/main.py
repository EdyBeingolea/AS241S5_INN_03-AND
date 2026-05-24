from app.core.deportes_rest import app
import uvicorn


def main():
    print("🚀 API iniciada en http://127.0.0.1:8000")

    uvicorn.run(
        host="127.0.0.1",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    main()