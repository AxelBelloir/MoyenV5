import sqlite3

conn = sqlite3.connect('utilisateurs.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL
)
''')
conn.close()
print("Base initialisée🗃️")

