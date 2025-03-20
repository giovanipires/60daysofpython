import json
from typing import Any

def salvar_dados(arquivo: str, dados: Any) -> None:
    """_summary_
    Salva os dados fornecidos em uma arquivo JSON
    Args:
        arquivo (str): Caminho para o arquivo JSON
        dados (Any): Dados que serão armazenados no arquivo
    """
    with open(arquivo, 'w', encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        
def carregar_dados(arquivo: str) -> Any:
    """_summary_
    Lê os dados do arquivo JSON
    Args:
        arquivo (str): Caminho do arquivos JSON

    Returns:
        Any: _Dados carregados e lidos do arquivo JSON
    """
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"O arquivo não foi encontrado, caminho do arquivo {arquivo}")
        return {}

# Corrigindo o dicionário
dados_exemplos = {"nome": "Giovani", "endereço": "Rua Maestro", "cidade": "Niterói", "estado": "RJ"}

nome_arquivo = "nome_giovani.json"

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)
print("Dados carregados: ", dados_carregados)
