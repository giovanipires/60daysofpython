import sqlite3

conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

print("Conexão estabelecida com sucesso.")

# cursor.execute("""
#                INSERT INTO personagens (nome, poder, universo)
#                VALUES ("Goku", 9000, "Dragon Ball")
#                """)

# cursor.execute("""
#                INSERT INTO personagens (nome, poder, universo)
#                VALUES ("Vegeta", 8000, "Dragon Ball")
#                """)

cursor.execute("""
               INSERT INTO personagens (nome, poder, universo)
               VALUES ("Kuririn", 7000, "Dragon Ball")
               """)

conexao.commit()

print("Dados inseridos com sucesso.")

cursor.close()
conexao.close()
