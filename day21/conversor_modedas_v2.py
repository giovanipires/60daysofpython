def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    Converte um valor de uma moeda para outra com base na taxa de câmbio fornecida.

    Args:
        valor (float): Valor que desejamos converter.
        taxa_cambio (float): Taxa de câmbio utilizada para a conversão.
        tipo_conversao (str): Tipo de conversão no formato 'moeda_origem_moeda_destino'.
                             Exemplo: 'dolar_real' para converter de dólar para real.

    Returns:
        float: Valor convertido.

    Raises:
        ValueError: Se o tipo de conversão for inválido ou se o valor ou taxa de câmbio forem negativos.
    """
    if valor < 0 or taxa_cambio < 0:
        raise ValueError("Valor e taxa de câmbio devem ser positivos.")

    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio, 2)
    else:
        raise ValueError("Tipo de conversão inválida. Use 'dolar_real' ou 'real_dolar'.")

def menu_conversao():
    """
    Exibe um menu para o usuário escolher a conversão desejada e insere o valor.
    """
    print("Bem-vindo ao Conversor de Moedas!")
    print("Escolha a conversão:")
    print("1 - Dólar para Real")
    print("2 - Real para Dólar")

    escolha = input("Digite o número da opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))
    taxa_cambio = float(input("Digite a taxa de câmbio atual: "))

    if escolha == '1':
        resultado = conversor_moeda(valor, taxa_cambio, 'dolar_real')
        print(f"{valor} dólares equivalem a {resultado} reais.")
    elif escolha == '2':
        resultado = conversor_moeda(valor, taxa_cambio, 'real_dolar')
        print(f"{valor} reais equivalem a {resultado} dólares.")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Executa o menu de conversão
menu_conversao()
