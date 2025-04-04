import sqlite3

conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

print("Conexão estabelecida com sucesso.")

cursor.execute("UPDATE personagens SET poder = 9500 WHERE id = 1")

conexao.commit()

print("Dados atualizados. \n")

cursor.execute("SELECT * FROM personagens WHERE id = 1")
consulta_update = cursor.fetchall()
print(consulta_update)

cursor.close()
conexao.close()
