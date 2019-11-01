import uvicorn

if __name__ == "__main__":
    from api.api import create_app
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
