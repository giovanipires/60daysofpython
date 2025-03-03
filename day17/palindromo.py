print("Bem vindo ao verificador de Palíndromo")

def palindromo(texto):
    """_summary_
    Uma função para verificar se palavra, texto ou número é um palídromo
    Args:
        texto (string): palavra, texto ou número.
        return: True, infromar em tela a texto e o palíndromo.
    """
    texto = str(texto).replace(" ", "").lower()

    if texto == texto[::-1]:
        return f"O {texto} é um palíndromo."
    return f"O {texto} não é um palíndromo."

entrada = input("Digite a palavra que deseja verificar: ")
print(palindromo(entrada))
