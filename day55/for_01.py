from colorama import Fore, Style
from random import randint

for i in range (1, 11):
    print(f'i = {i}')
    
for j in range(10):
    print('i = {}'.format(i))
    
for x in range(1,11):
    for z in range(1,11):
        print(f'{x} * {z} = {x * z}')