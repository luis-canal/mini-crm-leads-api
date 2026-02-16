import sqlite3

conn = sqlite3.connect("crm.db", check_same_thread=False)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    carro TEXT NOT NULL,
    status TEXT NOT NULL
)
""")

conn.commit()
