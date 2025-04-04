import sqlite3

conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

print("Conexão estabelecida com sucesso.")

cursor.execute("""
                CREATE TABLE IF NOT EXISTS personagens (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    poder INTEGER NOT NULL,
                    universo TEXT NOT NULL
                )
               """)

print ("A tabela foi criada com sucesso.")

conexao.close()

