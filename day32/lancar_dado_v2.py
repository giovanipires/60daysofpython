from random import randint

print("Simulação de lançamento de dados!")
print("Possuimos dados de 4, 6, 8, 10, 12 e 20 faces.")
dado = int(input("Qual dado você deseja lançar? "))
if dado in [4, 6, 8, 10, 12, 20]:
    print(f"O resultado do dado de {dado} faces foi: {randint(1, dado)}")
else:
    print("Dado inválido. Tente novamente.")
