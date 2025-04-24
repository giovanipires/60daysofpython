from colorama import Fore, Style
from random import randint

# while True:
#     print(Fore.GREEN + "Este é um laço infinito." + Style.RESET_ALL)
    
numro_informado = -1

numero_secreto = randint(0,9)

while numro_informado != numero_secreto:
    numro_informado = int(input(Fore.LIGHTBLACK_EX + 'Informe um número de 0 a 9: ' + Style.RESET_ALL))

print('Número secreto {} foi encontrato!'.format(numero_secreto))
