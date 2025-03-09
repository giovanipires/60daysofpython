import random
def jogar_adivinhacao():
    """_summary_
    Jogo onde o usuário terá de advinha um número aleatório gerado pelo computador.
    """
    print("Bem vindo ao jogo de adivinhação")
    print("Escolha um número entre 0 e 10")
    numero_secreto = random.randint(0, 10)
    tentativas = 0
    while True: 
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            if palpite < numero_secreto:
                print("O número secreto é maior")
            elif palpite > numero_secreto:
                print("O número secreto é menor")
            else:
                print(f"Parabéns, você acertou! O número era {numero_secreto}, suas tentativas foram {tentativas}")
                break
        except ValueError:
            print("Entrada inválida, por favor digite um número de 0 a 10")

if __name__ == "__main__":
    jogar_adivinhacao()
