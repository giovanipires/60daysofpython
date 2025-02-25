"""lista ordenada a partir do metodo sorted()"""

#1. lista numérica

lista_numerica = [1, 77, 63, 42, 99, 98, 66, 63, 62, 67, 83, 2, 3, 5, 8, 4, 12]
numeros_ordenados = sorted(lista_numerica)
numeros_ordenados_reverse = sorted(lista_numerica, reverse=True)
print(numeros_ordenados)
print(numeros_ordenados_reverse)

lista_palavras = ['Abelha', 'Cabalo', 'Beija-flor', 'Elefante', 'Zebra', 'Sapo', 'Raposa', 'Leão']
lista_ordenada = sorted(lista_palavras)
print(lista_ordenada)
