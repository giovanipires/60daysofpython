import re

print("Bem vindo ao 44º dia com Python \n Hoje vamos ver de REGEX ")

def validar_email(email):
    """Valida um endereço de email usando regex.
    
    Args:
        email (string): email a ser validado
        
    Returns:
        bool: True se o email é válido, False caso contrário
    """
    try:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None
    except TypeError:
        # Caso o email não seja uma string
        return False

def main():
    lista_emails = []
    
    print("Digite os emails (um por linha). Digite 'sair' para terminar:")
    try:
        while True:
            try:
                email = input("> ").strip()
                if email.lower() == 'sair':
                    break
                # Verifica se o campo não está vazio
                if not email:
                    print("Por favor, digite um email ou 'sair' para terminar.")
                    continue
                lista_emails.append(email)
            except KeyboardInterrupt:
                print("\nOperação interrompida pelo usuário. Parando a entrada de emails.")
                break
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                continue
    
    except Exception as e:
        print(f"Erro durante a entrada de dados: {e}")
        return
    
    # Validando cada email
    emails_validos = []
    emails_invalidos = []
    
    for email in lista_emails:
        try:
            if validar_email(email):
                emails_validos.append(email)
            else:
                emails_invalidos.append(email)
        except Exception as e:
            print(f"Erro ao validar o email {email}: {e}")
            emails_invalidos.append(email)
    
    # Mostrando os resultados
    print("\nEmails válidos:")
    for email in emails_validos:
        print(f"- {email}")
    
    print("\nEmails inválidos:")
    for email in emails_invalidos:
        print(f"- {email}")

if __name__ == "__main__":
    main()
