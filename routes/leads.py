from fastapi import APIRouter, Query, HTTPException
from schemas import LeadCreate, LeadUpdate
from services import leads_service
from database import cursor, conn


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

@router.patch("/leads/{lead_id}")
def atualizar_lead(lead_id: int, lead: LeadUpdate):

    # verifica se existe
    cursor.execute("SELECT * FROM leads WHERE id=?", (lead_id,))
    existing = cursor.fetchone()

    if not existing:
        raise HTTPException(status_code=404, detail="Lead não encontrado")

    # campos enviados
    campos = []
    valores = []

    for campo, valor in lead.model_dump(exclude_none=True).items():
        campos.append(f"{campo}=?")
        valores.append(valor)

    if not campos:
        raise HTTPException(status_code=400, detail="Nenhum campo enviado")

    valores.append(lead_id)

    query = f"""
    UPDATE leads
    SET {', '.join(campos)}
    WHERE id=?
    """

    cursor.execute(query, valores)
    conn.commit()

    return {"msg": "Lead atualizado com sucesso"}