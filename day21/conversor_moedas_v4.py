import requests

def buscar_taxa_cambio(moeda_origem, moeda_destino, api_key):
    """
    Busca a taxa de câmbio atual entre duas moedas usando a Exchange Rates API.
    No plano gratuito, a moeda base é fixa em EUR.

    Args:
        moeda_origem (str): Código da moeda de origem (ex: 'USD').
        moeda_destino (str): Código da moeda de destino (ex: 'BRL').
        api_key (str): Chave de API para acessar o serviço.

    Returns:
        float: Taxa de câmbio atual.

    Raises:
        Exception: Se houver erro na requisição à API.
    """
    # No plano gratuito, a moeda base é sempre EUR
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols={moeda_origem},{moeda_destino}"
    print(f"URL da requisição: {url}")  # Debug: Mostra a URL sendo usada

    resposta = requests.get(url)

    # Verifica o status da resposta
    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Resposta da API: {dados}")  # Debug: Mostra a resposta completa da API

        if dados.get("success", False):
            # Obtém as taxas de câmbio para a moeda de origem e destino
            taxa_origem = dados["rates"][moeda_origem]
            taxa_destino = dados["rates"][moeda_destino]
            # Calcula a taxa de câmbio indireta
            return taxa_destino / taxa_origem
        else:
            raise Exception(f"Erro na API: {dados.get('error', {}).get('info', 'Erro desconhecido')}")
    else:
        raise Exception(f"Erro na requisição: {resposta.status_code} - {resposta.text}")

def conversor_moeda(valor, taxa_cambio):
    """
    Converte um valor de uma moeda para outra com base na taxa de câmbio.

    Args:
        valor (float): Valor que desejamos converter.
        taxa_cambio (float): Taxa de câmbio utilizada para a conversão.

    Returns:
        float: Valor convertido.
    """
    return round(valor * taxa_cambio, 2)

def menu_conversao(api_key):
    """
    Exibe um menu para o usuário escolher a conversão desejada e insere o valor.
    """
    print("Bem-vindo ao Conversor de Moedas!")
    print("Escolha a conversão:")
    print("1 - Dólar (USD) para Real (BRL)")
    print("2 - Real (BRL) para Dólar (USD)")
    print("3 - Euro (EUR) para Real (BRL)")
    print("4 - Real (BRL) para Euro (EUR)")
    print("5 - Dólar (USD) para Euro (EUR)")
    print("6 - Euro (EUR) para Dólar (USD)")

    escolha = input("Digite o número da opção desejada: ")
    valor = float(input("Digite o valor a ser convertido: "))

    try:
        if escolha == '1':
            taxa_cambio = buscar_taxa_cambio("USD", "BRL", api_key)
            resultado = conversor_moeda(valor, taxa_cambio)
            print(f"{valor} dólares equivalem a {resultado} reais.")
        elif escolha == '2':
            taxa_cambio = buscar_taxa_cambio("BRL", "USD", api_key)
            resultado = conversor_moeda(valor, 1 / taxa_cambio)  # Inverte a taxa para conversão inversa
            print(f"{valor} reais equivalem a {resultado} dólares.")
        elif escolha == '3':
            taxa_cambio = buscar_taxa_cambio("EUR", "BRL", api_key)
            resultado = conversor_moeda(valor, taxa_cambio)
            print(f"{valor} euros equivalem a {resultado} reais.")
        elif escolha == '4':
            taxa_cambio = buscar_taxa_cambio("BRL", "EUR", api_key)
            resultado = conversor_moeda(valor, 1 / taxa_cambio)  # Inverte a taxa para conversão inversa
            print(f"{valor} reais equivalem a {resultado} euros.")
        elif escolha == '5':
            taxa_cambio = buscar_taxa_cambio("USD", "EUR", api_key)
            resultado = conversor_moeda(valor, taxa_cambio)
            print(f"{valor} dólares equivalem a {resultado} euros.")
        elif escolha == '6':
            taxa_cambio = buscar_taxa_cambio("EUR", "USD", api_key)
            resultado = conversor_moeda(valor, 1 / taxa_cambio)  # Inverte a taxa para conversão inversa
            print(f"{valor} euros equivalem a {resultado} dólares.")
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 6.")
    except Exception as e:
        print(f"Erro: {e}")

# Substitua 'SUA_CHAVE_DE_API' pela sua chave de API
API_KEY = "SUA_CHAVE_DE_API"

# Executa o menu de conversão
menu_conversao(API_KEY)
