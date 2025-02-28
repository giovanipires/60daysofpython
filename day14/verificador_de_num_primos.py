"""Verificador de números primos"""
print('Bem vindo ao nosso verificador de núermos primos!')
numero = int(input("Digite o número a ser verificado como nº primo: "))
#assumiremos por default uma variável como nº primo
eh_primo = True

if numero <= 1:
    eh_primo = False

for i in range(2, int(numero ** 0.5) + 1): #testamops apenas até a raiz quadrada
    if numero % i == 0: #se o nº for divisilve por i
        eh_primo = False #não é primo
        break #saimos do loop, pois já encontramos um divisor

if eh_primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
