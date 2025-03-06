def transpor_matriz(matriz):
    """_summary_
    Gerar uma matriz transposta de 3 x 3
    Substituir colulas horizontais por verticais
    
    Args:
        Matriz (list): 3 X 3
    Return:
        Matriz transposta
    Raises:
        ValueErros: Se não tiver matriz 3 x 3
    """
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz não possui o tamanho de 3X3")

    #gerar a matriz transposta
    transposta = [[matriz[j][i] for j in range (3)] for i in range(3)]
    return transposta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in transpor_matriz(matriz):
    print(linha)
