
def calcular_imc():
    """
    Funcao que calcula o IMC
    """

    print("Bem vindos a calculadora de IMC")

    try:
        peso = float(input("Digite o seu peso em quilogramas: "))

        altura = float(input("Digite sua altura em metros: "))

        if peso < 0 or altura < 0:
            print("O peso e altura deve ser maior que O")
            return #encerrar a funcao
    
        imc = round(peso / (altura ** 2), 2)

        #Reduzi a a redundância nas condições, já que o elif só é avaliado se a condição anterior for falsa.
        if imc < 18.5:
            print(f"Seu IMC é {imc}, você está abaixo do peso ideal")
        elif imc < 24.9:
            print(f"Seu IMC é {imc}, você está no peso normal")
        elif imc < 29.9:
            print(f"Seu IMC é {imc}, você está com sobrepeso")
        else:
            print(f"Seu IMC é {imc}, você está com obesidade")

    except ValueError:
        print("A entrada esta invalida")


# Significa que estamos rodando esse codigo internamente 
# Apenas roda se eu rodar o meu script calcular_imc 
if __name__ == "__main__":
    calcular_imc()
