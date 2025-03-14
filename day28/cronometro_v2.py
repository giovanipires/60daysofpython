import time

print('Bem vindo ao cronômetro!\n')
print('Caso deseja um cronômetro progressivo, digite 1.')
print('Caso deseja um cronômetro regressivo, digite 2.')
print('Caso deseja sair, digite 3.')
opcao = input('Digite a opção desejada: ')

def cronometro(tempo):
    """
    Função que cria um cronômetro progressivo ou regressivo, dependendo da opção escolhida pelo usuário.
    
    Args:
        tempo (int): Recebe um tempo em segundos para iniciar o processo de cronometragem.
    """
    print('Cronometro iniciado!')
    if opcao == '1':
        for i in range(1, tempo + 1):
            print(f'{i} segundos decorridos.')
            time.sleep(1)
        print('Fim do tempo!')
    elif opcao == '2':
        for i in range(tempo, 0, -1):
            print(f'{i} segundos restantes!')
            time.sleep(1)
        print('Fim do tempo!')

if opcao in ['1', '2']:
    try:
        tempo = int(input('Defina o tempo em segundos e pressione enter para iniciar o cronômetro: '))
        cronometro(tempo)
    except ValueError:
        print('Por favor, insira um número válido.')
elif opcao == '3':
    print('Saindo...')
else:
    print('Opção inválida!')
