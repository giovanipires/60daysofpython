"""generator"""

import sys

limite = int(1000)

def contador_com_yeld(limite):
    """contador infinito com utilização do yeld"""
    contador = int(0)
    while contador < limite: #while True é um loop infinito
        yield contador
        contador = contador + 1

print(type(contador_com_yeld(limite)))

#iteração pelo gerador
# for valor in contador_com_yeld(limite):
#     print(valor)

#contador com lista, ela diferente do yeld utiliza memória infinitamente, o que estoura a memória

def contador_com_lista(limite):
    """contador infinito com utilização de lista"""
    contador = int(0)
    lista = []
    while contador < limite: #while True é um loop infinito
        lista.append(contador)
        contador =+ 1
    return lista

lista_numeros = contador_com_lista(limite)
tamanho_lista = sys.getsizeof(lista_numeros)
print(f"Tamanho da lista em memória: {tamanho_lista} bytes.")

gerador_numeros = contador_com_yeld(limite)
tamanho_lista = sys.getsizeof(gerador_numeros)
print(f"Tamanho da lista em memória: {gerador_numeros} bytes.")

gerador = (x * x for x in range(10))
print(type(gerador))
#generator sempre será um iterador
for valor in gerador:
    print(valor)

#travou meu PC