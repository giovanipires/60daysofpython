from colorama import Fore, Style

print("De volta à escola, vamos ao seu boletim.")

def nota_conceito(valor):
    """Retorna o conceito correspondente à nota informada com formatação de cores.
    
    Args:
        valor (str): Nota numérica entre 0 e 10
        
    Returns:
        str: Conceito formatado com cor ou mensagem de erro
        
    Escala de conceitos:
        A   10.0 - 9.1    Verde
        A-  9.0 - 8.1      Verde
        B   8.0 - 7.1      Ciano
        B-  7.0 - 6.1      Ciano
        C   6.0 - 5.1      Amarelo
        C-  5.0 - 4.1      Amarelo
        D   4.0 - 3.1      Vermelho
        D-  3.0 - 2.1      Vermelho
        E   2.0 - 1.1      Vermelho
        E-  1.0 - 0.0      Vermelho
    """
    try:
        nota = float(valor)
        
        if nota > 10 or nota < 0:
            return f"{Fore.BLUE}Nota inválida (deve ser entre 0 e 10){Style.RESET_ALL}"
        elif nota >= 9.1:
            return f"{Fore.GREEN}A{Style.RESET_ALL}"
        elif nota >= 8.1:
            return f"{Fore.GREEN}A-{Style.RESET_ALL}"
        elif nota >= 7.1:
            return f"{Fore.CYAN}B{Style.RESET_ALL}"
        elif nota >= 6.1:
            return f"{Fore.CYAN}B-{Style.RESET_ALL}"
        elif nota >= 5.1:
            return f"{Fore.YELLOW}C{Style.RESET_ALL}"
        elif nota >= 4.1:
            return f"{Fore.YELLOW}C-{Style.RESET_ALL}"
        elif nota >= 3.1:
            return f"{Fore.RED}D{Style.RESET_ALL}"
        elif nota >= 2.1:
            return f"{Fore.RED}D-{Style.RESET_ALL}"
        elif nota >= 1.1:
            return f"{Fore.RED}E{Style.RESET_ALL}"
        else:  # 0.0 - 1.0
            return f"{Fore.RED}E-{Style.RESET_ALL}"
            
    except ValueError:
        return f"{Fore.RED}Erro: Por favor, informe um valor numérico válido{Style.RESET_ALL}"

if __name__ == "__main__":
    valor_informado = input("Informe sua nota para apresentarmos o conceito: ")
    conceito = nota_conceito(valor_informado)
    print(conceito)
