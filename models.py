from pydantic import BaseModel, Field
from typing import Literal


class LeadCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    telefone: str = Field(..., min_length=8, max_length=20)
    carro: str = Field(..., min_length=2, max_length=100)


class LeadResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    carro: str
    status: str


class StatusUpdate(BaseModel):
    status: Literal["novo", "contatado", "vendido", "perdido"]