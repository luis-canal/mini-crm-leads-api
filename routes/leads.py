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
    return cursor.fetchall()


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