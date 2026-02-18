from fastapi import FastAPI, Request
from routes.leads import router
from fastapi.responses import JSONResponse
from logger import logger

app = FastAPI()

app.include_router(router)

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):

    logger.error(
        f"Erro não tratado | "
        f"Endpoint: {request.method} {request.url} | "
        f"Erro: {str(exc)}"
    )

    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno do servidor"}
    )

@app.get("/")
def home():
    return {"msg": "Mini CRM API rodando 🚀"}