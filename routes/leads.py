from fastapi import APIRouter, Query
from database import cursor, conn

router = APIRouter()

@router.post("/leads")
def criar_lead(lead: dict):
    cursor.execute(
        "INSERT INTO leads (nome, telefone, carro, status) VALUES (?, ?, ?, ?)",
        (lead["nome"], lead["telefone"], lead["carro"], "novo")
    )
    conn.commit()
    return {"msg": "Lead criado"}


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
def atualizar_status(lead_id: int, status: str):
    cursor.execute(
        "UPDATE leads SET status=? WHERE id=?",
        (status, lead_id)
    )
    conn.commit()
    return {"msg": "Atualizado"}


@router.delete("/leads/{lead_id}")
def deletar(lead_id: int):
    cursor.execute("DELETE FROM leads WHERE id=?", (lead_id,))
    conn.commit()
    return {"msg": "Deletado"}