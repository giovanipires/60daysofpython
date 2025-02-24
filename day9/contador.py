"""Criando uma função de contador personalizado."""
def contador_personalizado():
    """função para realizar uma contagem limitada"""
    try:
        limite = int(input("Digite o valor máximo do contador: "))
         #função range cria uma lista de número a partir do zero até o valor definido pelo usuário
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("entrada inválida. Por favor insira um número inteiro")

contador_personalizado()
