entrada = input("Digite o número para validação: ")

try:
    numero = int(entrada)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
except ValueError:
    print(f"O valor digitado, {entrada}, não é um número. Por favor verifique!")