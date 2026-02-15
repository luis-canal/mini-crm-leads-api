from fastapi import APIRouter, Query
from database import cursor, conn
from models import LeadCreate, LeadResponse, StatusUpdate, LeadStats

router = APIRouter()

@router.post("/leads", response_model=LeadResponse)
def criar_lead(lead: LeadCreate):

    cursor.execute(
        "INSERT INTO leads (nome, telefone, carro, status) VALUES (?, ?, ?, ?)",
        (lead.nome, lead.telefone, lead.carro, "novo")
    )
    conn.commit()

    lead_id = cursor.lastrowid

    return {
        "id": lead_id,
        "nome": lead.nome,
        "telefone": lead.telefone,
        "carro": lead.carro,
        "status": "novo"
    }


@router.get("/leads")
def listar_leads(
    status: str = Query(None),
    carro: str = Query(None),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0)
):

    query = "SELECT * FROM leads"
    filtros = []
    valores = []

    if status:
        filtros.append("status = ?")
        valores.append(status)

    if carro:
        filtros.append("carro = ?")
        valores.append(carro)

    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    query += " LIMIT ? OFFSET ?"
    valores.append(limit)
    valores.append(offset)

    cursor.execute(query, tuple(valores))
    dados = cursor.fetchall()

    leads = []
    for lead in dados:
        leads.append({
            "id": lead[0],
            "nome": lead[1],
            "telefone": lead[2],
            "carro": lead[3],
            "status": lead[4]
        })

    return leads

@router.put("/leads/{lead_id}")
def atualizar_status(lead_id: int, status_update: StatusUpdate):

    cursor.execute(
        "UPDATE leads SET status=? WHERE id=?",
        (status_update.status, lead_id)
    )
    conn.commit()

    return {"msg": "Status atualizado"}


@router.delete("/leads/{lead_id}")
def deletar(lead_id: int):
    cursor.execute("DELETE FROM leads WHERE id=?", (lead_id,))
    conn.commit()
    return {"msg": "Deletado"}

@router.get("/leads/stats", response_model=LeadStats)
def estatisticas():

    cursor.execute("SELECT COUNT(*) FROM leads")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE status='novo'")
    novos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE status='contatado'")
    contatados = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE status='vendido'")
    vendidos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM leads WHERE status='perdido'")
    perdidos = cursor.fetchone()[0]

    taxa = 0
    if total > 0:
        taxa = round((vendidos / total) * 100, 2)

    return {
        "total_leads": total,
        "novos": novos,
        "contatados": contatados,
        "vendidos": vendidos,
        "perdidos": perdidos,
        "taxa_conversao": taxa
    }