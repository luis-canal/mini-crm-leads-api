from fastapi import APIRouter, Query, HTTPException, Depends
from schemas import LeadCreate, LeadUpdate
from services import leads_service
from database import cursor, conn
from logger import logger
from security import verify_api_key


router = APIRouter()

@router.post("/leads")
def criar_lead(
    lead: LeadCreate,
    api_key: str = Depends(verify_api_key)
    ):

    try:
        cursor.execute(
            "INSERT INTO leads (nome, telefone, carro, status) VALUES (?, ?, ?, ?)",
            (lead.nome, lead.telefone, lead.carro, "novo")
        )
        conn.commit()

        lead_id = cursor.lastrowid

        logger.info(f"Lead criado com ID {lead_id}")

        return {"id": lead_id}

    except Exception as e:
        logger.error(f"Erro ao criar lead: {str(e)}")
        raise


@router.get("/leads")
def listar_leads(
    status: str = None,
    carro: str = None,
    page: int = 1,
    limit: int = 10,
    api_key: str = Depends(verify_api_key)
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
def atualizar_lead(lead_id: int, lead: LeadUpdate, api_key: str = Depends(verify_api_key)):

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
    SET {', '.join(campos)}, updated_at=CURRENT_TIMESTAMP
    WHERE id=?
    """

    cursor.execute(query, valores)
    conn.commit()

    logger.info(f"Lead atualizado com sucesso: ID {lead_id}")

    return {"msg": "Lead atualizado com sucesso"}

@router.delete("/leads/{lead_id}")
def deletar_lead(lead_id: int, api_key: str = Depends(verify_api_key)):

    cursor.execute(
        "SELECT * FROM leads WHERE id=? AND deleted=0",
        (lead_id,)
    )
    lead = cursor.fetchone()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead não encontrado")

    cursor.execute(
        "UPDATE leads SET deleted=1 WHERE id=?",
        (lead_id,)
    )
    conn.commit()

    logger.warning(f"Lead marcado como deletado: ID {lead_id}")

    return {"msg": "Lead deletado com sucesso"}