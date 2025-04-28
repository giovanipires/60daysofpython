#Dado de 6 entre um e seis
#se for impar pare
#se for par e igual ao sorteado
#pela função dado impar e acertou e depois chamar break
#se não acertar chamar else

from random import randint

print("Bem vindo ao rolar de dados")

def sortear_dado():
    return randint(1,6)

for i in range(1,7):
    if i % 2 == 1:
        continue
    
    if sortear_dado() == i:
        print('Acertou', i)
        break

else:
    print('Não acertou o resultado')
