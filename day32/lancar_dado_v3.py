from random import randint

def lancar_dado(faces):
    """Função para lançar um dado com o número de faces especificado."""
    return randint(1, faces)

def obter_entrada_usuario():
    """Função para obter e validar a entrada do usuário."""
    while True:
        try:
            dado = int(input("Qual dado você deseja lançar? "))
            if dado in [4, 6, 8, 10, 12, 20]:
                return dado
            else:
                print("Dado inválido. Os valores válidos são: 4, 6, 8, 10, 12 e 20.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def main():
    print("Simulação de lançamento de dados!")
    print("Possuimos dados de 4, 6, 8, 10, 12 e 20 faces.")

    dado = obter_entrada_usuario()
    resultado = lancar_dado(dado)
    print(f"O resultado do dado de {dado} faces foi: {resultado}")

if __name__ == "__main__":
    main()
