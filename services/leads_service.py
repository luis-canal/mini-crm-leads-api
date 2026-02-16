from database import cursor, conn

def criar_lead(nome, telefone, carro, status):
    cursor.execute(
        "INSERT INTO leads (nome, telefone, carro, status) VALUES (?, ?, ?, ?)",
        (nome, telefone, carro, status)
    )
    conn.commit()
    return cursor.lastrowid


def listar_leads(filtros, limit, offset):
    query = "SELECT * FROM leads WHERE 1=1"
    params = []

    if filtros.get("status"):
        query += " AND status = ?"
        params.append(filtros["status"])

    if filtros.get("carro"):
        query += " AND carro = ?"
        params.append(filtros["carro"])

    query += " LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    cursor.execute(query, params)

    return cursor.fetchall()


def estatisticas():
    cursor.execute("""
        SELECT status, COUNT(*) as total
        FROM leads
        GROUP BY status
    """)

    return cursor.fetchall()