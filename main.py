from fastapi import FastAPI
from routes.leads import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"msg": "Mini CRM API rodando 🚀"}