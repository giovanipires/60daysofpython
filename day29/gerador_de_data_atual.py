from datetime import datetime
import pytz

def exibir_data_hora_atual():
    """
    Função que exibe a data e hora atual
    """
    fuso_horario = pytz.timezone('America/Sao_Paulo')
    
    data_hora = datetime.now(fuso_horario)
    data_hora_formatada = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    
    print(f'Data e hora atual: {data_hora_formatada}')
    
if __name__ == '__main__':
    exibir_data_hora_atual()
