def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """_summary_
    Essa função será utilizada para a conversão de valores / câmbio;
    Args:
        valor (float): Valor que desejamos converter
        taxa_cambio (float): A taxa utilizada para a conversão
        tipo_conversao (string): De qual moeda para qual moeda estamos convertendo.
    Return:
        conversão(float): Valor já convertido
    Raises:
        ValueError: Se o tipo de conversão for errado
    """
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("Tipo de conversão inválida")

print(conversor_moeda(12, 6.1, 'dolar_real'))
