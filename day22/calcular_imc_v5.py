
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
        
        #Usei o match-case, uma opção mais nova, pythpn 3.10, para classificar o IMC, o que torna o código mais legível e fácil de reutilizar.
        #Sintaxe mais limpa e moderna, mas só disponível em versões mais recentes do Python.
        def classificar_imc(imc):
            match imc:
                case _ if imc < 18.5:
                    return f"Seu IMC é {imc}, você está abaixo do peso ideal"
                case _ if imc < 24.9:
                    return f"Seu IMC é {imc}, você está no peso normal"
                case _ if imc < 29.9:
                    return f"Seu IMC é {imc}, você está com sobrepeso"
                case _:
                    return f"Seu IMC é {imc}, você está com obesidade"

        print(classificar_imc(imc))

    except ValueError:
        print("A entrada esta invalida")

# Significa que estamos rodando esse codigo internamente 
# Apenas roda se eu rodar o meu script calcular_imc 
if __name__ == "__main__":
    calcular_imc()
