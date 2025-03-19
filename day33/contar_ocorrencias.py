from collections import Counter
"""""Importando a função counter da bibliotéca collections"""
def contar_ocorrencias(lista):
    """
    Uma função que realiza a contagem de itens em uma lista 
    Args:
        Lista (list): objetos contidos em uma listagem
    """
    contagem = Counter(lista)

    for elemento, quantidade, in contagem.items():
        print(f"{elemento}: {quantidade}")

    return "Contagem realizada com sucesso."

if __name__ == "__main__":
    lista_exemplo = ['banana', 'laranja', 'uva', 'laranja', 'pera', 'abacaxi', 'mixirica','uva', 'pera']

    print(contar_ocorrencias(lista_exemplo))
