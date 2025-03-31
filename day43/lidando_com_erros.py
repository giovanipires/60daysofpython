def dividir(numerador, denominador):
    """_summary_
    Função simples de divisão.
    Args:
        numerador (number): Número que desejamos dividir
        denominador (number): Número pelo qual iremos dividir
    """
    try:
        resultado = numerador / denominador
        print(f"O resultado da divisão de {numerador} por {denominador} é: {resultado}")
    except ZeroDivisionError:
        print("A divisão por erro não pode ocorrer.")
    except TypeError:
        print("O código não pode aceitar caracteres, apenas números!")

print("Bem vindo, este é o 43º dia de Python. \n e estamos trabalhando com tratamento de exceções")
numerador = input("Informe o número que deseja dividir: ")
denominador = input("Informe o número que será o divisor: ")

if __name__ == "__main__":
    dividir(numerador,denominador)
