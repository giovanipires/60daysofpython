"""Conversor de Temperatura"""

def celsius_to_fahrenheit(celsius):
    """Converte uma temperatura de Celsius para Fahrenheit.

    Args:
        celsius (float): Valor da temperatura em Celsius.

    Returns:
        float: Valor da temperatura convertida para Fahrenheit.
    """
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converte uma temperatura de Fahrenheit para Celsius.

    Args:
        fahrenheit (float): Valor da temperatura em Fahrenheit.

    Returns:
        float: Valor da temperatura convertida para Celsius.
    """
    return (fahrenheit - 32) * 5/9


def get_temperature_input(prompt):
    """Solicita ao usuário uma temperatura e valida a entrada.

    Args:
        prompt (str): Mensagem exibida ao usuário.

    Returns:
        float: Valor da temperatura inserida pelo usuário.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")


def main():
    """Função principal do Conversor de Temperatura."""
    print("Bem-vindo ao Conversor de Temperatura!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Sair")

        choice = input("Escolha 1, 2 ou 3: ")

        if choice == "1":
            temperatura = get_temperature_input("Entre com a temperatura em Celsius: ")
            print(f"{temperatura}° Celsius é igual a {celsius_to_fahrenheit(temperatura)}° Fahrenheit")
        elif choice == "2":
            temperatura = get_temperature_input("Entre com a temperatura em Fahrenheit: ")
            print(f"{temperatura}° Fahrenheit é igual a {fahrenheit_to_celsius(temperatura)}° Celsius")
        elif choice == "3":
            print("Obrigado por usar o Conversor de Temperatura. Até logo!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()