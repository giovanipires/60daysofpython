
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
        
        #Usei uma função para classificar o IMC, o que torna o código mais legível e fácil de reutilizar.
        #Facilitará a reutilização do código e melhora organização, especialmente em programas maiores.
        def classificar_imc(imc):
            if imc < 18.5:
                return f"Seu IMC é {imc}, você está abaixo do peso ideal"
            elif imc < 24.9:
                return f"Seu IMC é {imc}, você está no peso normal"
            elif imc < 29.9:
                return f"Seu IMC é {imc}, você está com sobrepeso"
            else:
                return f"Seu IMC é {imc}, você está com obesidade"

        print(classificar_imc(imc))

    except ValueError:
        print("A entrada esta invalida")

# Significa que estamos rodando esse codigo internamente 
# Apenas roda se eu rodar o meu script calcular_imc 
if __name__ == "__main__":
    calcular_imc()
