from fastapi import APIRouter
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
def listar_leads():
    cursor.execute("SELECT * FROM leads")
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