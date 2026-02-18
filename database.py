import sqlite3

conn = sqlite3.connect("crm.db", check_same_thread=False)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    carro TEXT,
    status TEXT DEFAULT 'novo',
    deleted INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

conn.commit()
