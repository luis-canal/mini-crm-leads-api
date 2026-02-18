from fastapi import FastAPI, Request
from routes.leads import router
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Erro interno do servidor"}
    )

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"msg": "Mini CRM API rodando 🚀"}