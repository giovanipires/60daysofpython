import time

def cronometro_de_dez_segundos():
    """_summary_
    Realiza uma contagem regressiva de 10 segundos.
    """
    print('Cronômetro de 10 segundos iniciando!')
    for i in range(10, 0, -1):
        print(f"Tempo restante: {i} segundos.", end='\r', flush=True)
        time.sleep(1)
    print('Cronômetro finalizado!')
    
if __name__ == '__main__':
    cronometro_de_dez_segundos()