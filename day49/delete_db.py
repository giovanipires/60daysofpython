import sqlite3

conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

print("Conexão estabelecida com sucesso.")

cursor.execute("DELETE FROM personagens WHERE id = 3")

conexao.commit()

print("Exclusão realizada com sucesso.")

cursor.close()
conexao.close()
