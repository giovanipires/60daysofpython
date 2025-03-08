
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
        
        #Usei um dicionário para armazenar os intervalos de IMC e suas respectivas mensagens.
        #Facilita a manutenção, pois podemos adicionar ou remover intervalos sem alterar a lógica principal.
        imc_ranges = {
            (0, 18.5): f"Seu IMC é {imc}, você está abaixo do peso ideal",
            (18.5, 24.9): f"Seu IMC é {imc}, você está no peso normal",
            (25, 29.9): f"Seu IMC é {imc}, você está com sobrepeso",
            (30, float('inf')): f"Seu IMC é {imc}, você está com obesidade"
        }

        for (min_val, max_val), message in imc_ranges.items():
            if min_val <= imc < max_val:
                print(message)
                break

    except ValueError:
        print("A entrada esta invalida")

# Significa que estamos rodando esse codigo internamente 
# Apenas roda se eu rodar o meu script calcular_imc 
if __name__ == "__main__":
    calcular_imc()
