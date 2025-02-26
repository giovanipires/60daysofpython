"""Dia 12 do desafio de 60 dias em Python"""

def busca_linear(lista, numero_procurado):
    """
        Procurar um número dentro de uma lista utilizando busca linear

        :param lista: lista de números
        :param numero_procuado: o número que desejamos localizar
    """
    for i, numero in enumerate(lista): #função nativa do python
        #enumerate passa por cada item detro de uma lista, enquanto contabiliza
        if numero == numero_procurado:
            return i
    return -1

# lista = [10, 2, 8, 4, 6 ,9, 11, 3]
# numero_procurado = 8

buscando_o_numero = busca_linear(lista=[10, 2, 8, 4, 6 ,9, 11, 3], numero_procurado=3)

if buscando_o_numero != -1:
    print(f'O número se encontra no índice: {buscando_o_numero}')
else:
    print('Não encontrador.')

# for i, numero in enumerate([1,2,3,4,5,6,7,8,9]):
#     print(f"Indíce: {i} e objeto da lista: {numero}")
