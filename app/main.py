from fastapi import FastAPI, Request
from app.routes.leads import router
from fastapi.responses import JSONResponse
from app.logger import logger
from app.config import APP_NAME, VERSION

app = FastAPI(
    tittle=APP_NAME,
    version=VERSION
)

@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "ok",
        "service": "mini-crm-leads-api"
    }

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