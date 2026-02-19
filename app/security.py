from fastapi import Header, HTTPException
from app.config import API_KEY

def verify_api_key(x_api_key: str = Header(None)):

    if x_api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API KEY obrigatória"
        )
    
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="API Key inválida"
        )
    
    return x_api_key