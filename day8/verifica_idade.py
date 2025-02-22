"""Module providing a function printing python version."""
#Criando uma função para verificar idade
def verifica_idade(idade: int):
    """Function printing python version."""
    if idade >= 18:
        return True
    else:
        return False
try:
    input_user = int(input("Informe sua idade: "))
    print(verifica_idade(input_user))
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
