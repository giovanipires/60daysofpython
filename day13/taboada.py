"""Criando uma taboada de forma simples."""
print("Bem-vindo ao tabuada Python!")
numero = int(input("Informe o número que deseja saber a taboada: "))
print(f'Vamos a taboada do número: {numero}')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')