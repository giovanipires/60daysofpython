import re

print("Bem vindo a 44º dia com Python \n Hoje vamos ver de REGEX ")

def validar_email(email):
    """_summary_
    Função para a validação de emails
    Args:
        email (string): email digitado
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        print(f"O {email} é validado.")
    else:
        print(f"O {email} não é validado.")

# Exemplos de uso:
emails = [
    "usuario@exemplo.com",
    "nome.sobrenome@dominio.com.br",
    "email+tag@exemplo.com",
    "email_invalido@",
    "outro@invalido."
]

for email in emails:
    print(f"{email}: {'Válido' if validar_email(email) else 'Inválido'}")