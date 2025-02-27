# o que é um fatorial?
#é um cálculo matemático onde multiplicamos os valores a partir
#do número passado.
#exemplo 5! = 5 x 4 x 3 x 2 x 1 = 120
#exemplo 3! = 3 x 2 x 1 = 6

def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão.
    
    : param n:Número inteiro não negativo.
    :return: Fatorial de n.
    """
    if n < 0:
        raise ValueError("O número deve ser positivo.")

    #então essa condicional retorna 1 se caso o número da função for 0 ou 1
    if n == 0 or n == 1:
        return 1

    #recursividade
    return n * fatorial(n - 1)

try:
    n = int(input('Informe o número que deseja que seja calculado o fatorial: '))
    print(fatorial(n))
except ValueError as e:
    print(e)
