from pydantic import BaseModel
from typing import Optional

class LeadCreate(BaseModel):
    nome: str
    telefone: str
    carro: str
    status: str

class LeadResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    carro: str
    status: str

class EstatisticaResponse(BaseModel):
    status: str
    total: int

class LeadUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    carro: Optional[str] = None
    status: Optional[str] = None