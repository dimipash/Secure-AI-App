from src.app import app

if __name__ == "__main__":
    import uvicorn

    run = uvicorn.run(app, host="0.0.0.0", port=8000)
     