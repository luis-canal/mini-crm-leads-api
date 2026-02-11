from fastapi import FastAPI
import sqlite3

app = FastAPI()

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    carro TEXT,
    status TEXT
)
""")
conn.commit()


@app.post("/leads")
def criar_lead(lead: dict):
    cursor.execute(
        "INSERT INTO leads (nome, telefone, carro, status) VALUES (?, ?, ?, ?)",
        (lead["nome"], lead["telefone"], lead["carro"], "novo")
    )
    conn.commit()
    return {"msg": "Lead criado"}


@app.get("/leads")
def listar_leads():
    cursor.execute("SELECT * FROM leads")
    return cursor.fetchall()


@app.put("/leads/{lead_id}")
def atualizar_status(lead_id: int, status: str):
    cursor.execute(
        "UPDATE leads SET status=? WHERE id=?",
        (status, lead_id)
    )
    conn.commit()
    return {"msg": "Atualizado"}


@app.delete("/leads/{lead_id}")
def deletar(lead_id: int):
    cursor.execute("DELETE FROM leads WHERE id=?", (lead_id,))
    conn.commit()
    return {"msg": "Deletado"}
