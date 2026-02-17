import sqlite3

conn = sqlite3.connect("crm.db", check_same_thread=False)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    telefone TEXT,
    carro TEXT,
    status TEXT,
    deleted INTEGER DEFAULT 0
)
""")
conn.commit()

conn.commit()
