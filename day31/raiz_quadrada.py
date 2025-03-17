import math

def raiz_quadrada(numero):
    """_summary_
    Calcula a raiz quadrada de um número.
    Args:
        numero (float): O númer para o qual a raiz quadrada será calculada.
    Returns:
        float_: _description_
    """
    if numero < 0:
        raise ValueError('O número deve ser positivo.')

    return round(math.sqrt(numero),2)

if __name__ == '__main__':
    try:
        print('Calculadora de raiz quadrada.')
        numero = float(input('Digite um número para calcular a raiz quadrada: '))
        print(f'A raiz quadrada de {numero} é {raiz_quadrada(numero)}')
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        print('Obrigado por usar a calculadora de raiz quadrada.')
# Output:
# Calculadora de raiz quadrada.
