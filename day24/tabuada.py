def tabuada():
    """
    Função que imprime a tabuada de 1 a 10
    Não temos entrada de dados inicialmente, pois desejamos que o usuário aponte sua necessidade.
    """
    print("Bem vindo ao seu gerador de tabuada!")
    print("Digite -1 para sair.")
    try:
        #solicitar número para o usuário
        entrada = int(input('Digite um número para gerar a tabuada dele de 1 a 10: '))

        if entrada == -1:
            print('Até mais!')
        elif entrada > 0:
            print(f'Tabuada do {entrada}: ')
            for i in range(1, 11):
                print(f'{entrada} x {i} = {entrada * i}')
        else:   raise ValueError

    except ValueError:
        print('Por favor digite um número inteiro positivo.')

if __name__ == '__main__':
    tabuada()
