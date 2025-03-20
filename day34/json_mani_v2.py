import json
from typing import Any, Dict

def salvar_dados(arquivo: str, dados: Dict[str, Any]) -> None:
    """
    Salva os dados fornecidos em um arquivo JSON.

    Args:
        arquivo (str): Caminho para o arquivo JSON.
        dados (Dict[str, Any]): Dados que serão armazenados no arquivo.

    Raises:
        TypeError: Se `dados` não for um dicionário.
    """
    if not isinstance(dados, dict):
        raise TypeError("Os dados devem ser um dicionário.")
    
    with open(arquivo, 'w', encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        
def carregar_dados(arquivo: str) -> Dict[str, Any]:
    """
    Lê os dados do arquivo JSON.

    Args:
        arquivo (str): Caminho do arquivo JSON.

    Returns:
        Dict[str, Any]: Dados carregados e lidos do arquivo JSON.

    Raises:
        json.JSONDecodeError: Se o arquivo JSON estiver corrompido.
    """
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"O arquivo não foi encontrado, caminho do arquivo {arquivo}")
        return {}
    except json.JSONDecodeError:
        print(f"O arquivo {arquivo} está corrompido ou mal formatado.")
        return {}

# Exemplo de uso
dados_exemplos = {"nome": "Giovani", "endereço": "Rua Maestro", "cidade": "Niterói", "estado": "RJ"}

nome_arquivo = "nome_giovani.json"

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)
print("Dados carregados: ", dados_carregados)
