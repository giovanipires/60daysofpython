import random

def jogar_adivinhacao():
    """
    Jogo de adivinhação onde o usuário tenta acertar um número aleatório gerado pelo computador.
    O número secreto está entre 0 e 10.
    O jogo informa se o palpite do usuário é maior ou menor que o número secreto.
    O jogo termina quando o usuário acerta o número ou desiste.
    """
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 0 e 10.")
    
    numero_secreto = random.randint(0, 10)
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite (ou -1 para desistir): "))
            
            if palpite == -1:
                print(f"Você desistiu. O número secreto era {numero_secreto}.")
                break
            
            if palpite < 0 or palpite > 10:
                print("Por favor, digite um número entre 0 e 10.")
                continue
            
            tentativas += 1
            
            if palpite < numero_secreto:
                print("O número secreto é maior.")
            elif palpite > numero_secreto:
                print("O número secreto é menor.")
            else:
                print(f"Parabéns, você acertou! O número era {numero_secreto}.")
                print(f"Você fez {tentativas} tentativas.")
                break
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    jogar_adivinhacao()
