from fastapi import APIRouter, Query
from schemas import LeadCreate
from services import leads_service

router = APIRouter()

@router.post("/leads")
def criar_lead(lead: LeadCreate):
    id = leads_service.criar_lead(
        lead.nome,
        lead.telefone,
        lead.carro,
        lead.status
    )

    return {"id": id}


@router.get("/leads")
def listar_leads(
    status: str = None,
    carro: str = None,
    page: int = 1,
    limit: int = 10
):
    offset = (page - 1) * limit

    filtros = {
        "status": status,
        "carro": carro
    }

    leads = leads_service.listar_leads(filtros, limit, offset)

    return leads


@router.get("/leads/stats")
def estatisticas():
    return leads_service.estatisticas()
