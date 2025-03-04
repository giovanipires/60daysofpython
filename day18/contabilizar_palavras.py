# Contador de palavras
print("Bem-vindo ao contador de palavras!")

def contar_palavras(texto):
    """
    Conta as palavras em uma string.
    
    Args:
        texto (string): Entrada realizada pelo usuário.
    
    Returns:
        int: Número de palavras identificadas.
    """
    # Separa as palavras utilizando o espaço entre elas
    palavras = texto.split()
    return len(palavras)

# Solicita a entrada do usuário
entrada = input("Digite o texto que deseja contar o número de palavras: ")

# Conta as palavras e exibe o resultado
numero_palavras = contar_palavras(entrada)
print(f"O número de palavras neste texto foi de: {numero_palavras}")
