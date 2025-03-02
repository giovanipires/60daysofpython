"""Vamos fazer o cálculo da sequência Fibonacci"""
fibonacci = [0, 1] #a sequência sempre começa com 0 e 1

for i in range(8):
    proximo_numero = fibonacci[-1] + fibonacci[-2] #soma um mais zero
    fibonacci.append(proximo_numero)

print(fibonacci)
