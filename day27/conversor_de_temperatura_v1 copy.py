"""Conversor de Temperatura"""

def celsius_to_fahrenheit(celsius):
    """_summary_

    Args:
        celsius (float): Receber um valor númerico em celsius

    Returns:
        float: Retorna o cálculo de celsius para fahrenheit
    """     
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """_summary
    
    Args:
        fahrenheit (float): Receber um valor númerico em fahrenheit
        
    Returns:
        float: Retorna o cálculo de fahrenheit para celsius
    """
    return (fahrenheit - 32) * 5/9

def main():
    """_summary
    
    Args:
        choice (str): Receber a escolha do usuário
        celsius (float): Receber a temperatura em celsius
        fahrenheit (float): Receber a temperatura em fahrenheit
    """
    print("Bem vindo ao Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")

    choice = input("Escolha 1 ou 2: ")  # Receber a escolha do usuário

    if choice == "1":
        temperatura = float(input("Entre com a temperatura em Celsius: "))  # Receber a temperatura em celsius
        print(f"{temperatura}° Celsius é igual a {celsius_to_fahrenheit(temperatura)}° Fahrenheit")
    elif choice == "2":
        temperatura = float(input("Entre com a temperatura em Fahrenheit: "))
        print(f"{temperatura}° Fahrenheit é igual a {fahrenheit_to_celsius(temperatura)}° Celsius")
    else:
        print("Escolha inválida")
    
    print("Obrigado por usar o Conversor de Temperatura")

if __name__ == "__main__":
    main()
