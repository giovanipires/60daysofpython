import time

print('Bem vindo ao cronômetro!')

def cronometro(tempo):
    """_summary_
    Função que cria um cronômetro regressivo.
    Args:
        tempo (time): Recebe um tempo em segundos para iniciar o processo de cronometragem.
    """
    print('Cronometro iniciado!')
    for i in range(tempo, 0, -1):
        print(f'{i} segundos restantes!')
        time.sleep(1)
    print('Fim do tempo!')

tempo = input('Defina o tempo em segundos e pressione enter para iniciar o cronômetro: ')

if __name__ == '__main__':
    cronometro(tempo)
