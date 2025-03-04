"""Calculadora de IMC"""
print("Bem vindo, vamos calcular seu IMC?")

# Função para calcular o IMC
def calcular_imc(peso, altura):
    """_summary_
    Calculadora de IMC
    Args:
        peso (float): peso em kilos da pessoa utilizando a calculadora
        altura (float): altura em metros da pessoa utilizando a calculadora

    Returns:
        float: resultado do cálculo do IMC
    """
    return peso / pow(altura, 2)

# Função para classificar o IMC
def classificar_imc(imc):
    """_summary_

    Args:
        imc (float): valor calculado do IMC

    Returns:
        string: descrição baseada em uma tabela existente
    """    
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Exemplo de uso
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"Seu IMC é {imc:.2f}, e sua classificação é: {classificacao}")
