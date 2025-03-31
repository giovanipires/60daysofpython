import re

print("Bem vindo a 44º dia com Python \n Hoje vamos ver de REGEX ")

def validar_email(email):
    """_summary_
    Função para a validação de emails
    Args:
        email (string): email digitado
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

lista_emails = []

print("Digite os emails (um por linha). Digite 'sair' para terminar):")
while True:
    email = input("> ").strip()
    if email.lower() == 'sair':
        break
    lista_emails.append(email)

# Validando cada email
emails_validos = []
emails_invalidos = []

for email in lista_emails:
    if validar_email(email):
        emails_validos.append(email)
    else:
        emails_invalidos.append(email)

# Mostrando os resultados
print("\nEmails válidos:")
for email in emails_validos:
    print(f"- {email}")

print("\nEmails inválidos:")
for email in emails_invalidos:
    print(f"- {email}")