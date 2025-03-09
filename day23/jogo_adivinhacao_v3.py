import random

def jogar_adivinhacao():
    """
    Jogo de adivinhação onde o usuário tenta acertar um número aleatório gerado pelo computador.
    O número secreto está entre 0 e 10.
    O usuário tem até 3 tentativas para acertar.
    O jogo informa se o palpite do usuário é maior ou menor que o número secreto.
    O jogo termina quando o usuário acerta o número ou esgota as tentativas.
    """
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 0 e 10.")
    print("Você tem apenas 3 tentativas. Boa sorte!")
    
    numero_secreto = random.randint(0, 10)
    tentativas_restantes = 3
    
    while tentativas_restantes > 0:
        try:
            print(f"\nTentativas restantes: {tentativas_restantes}")
            palpite = int(input("Digite seu palpite: "))
            
            if palpite < 0 or palpite > 10:
                print("Por favor, digite um número entre 0 e 10.")
                continue
            
            tentativas_restantes -= 1
            
            if palpite < numero_secreto:
                print("O número secreto é maior.")
            elif palpite > numero_secreto:
                print("O número secreto é menor.")
            else:
                print(f"Parabéns, você acertou! O número era {numero_secreto}.")
                print(f"Você conseguiu em {3 - tentativas_restantes} tentativas.")
                break
                
            if tentativas_restantes == 0:
                print(f"\nSuas tentativas acabaram! O número secreto era {numero_secreto}.")
                
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    jogar_adivinhacao()
