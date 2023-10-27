from fastapi import FastAPI
from fastapi.responses import JSONResponse


def create_api_app() -> FastAPI:
    app = FastAPI()
    
    @app.get("/healthy")
    async def healthcheck() -> JSONResponse:
        return JSONResponse({"status": "ok"})

    return app
