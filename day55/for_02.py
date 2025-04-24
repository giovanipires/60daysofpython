palavra = 'pindamonhangaba'

for letra in palavra:
    print(letra)

for letra in palavra:
    print(letra, end=',')
    
lista = ['Arghus', 'Tutu', 'Zé Droguinha', 'Carol']

for nomes in lista:
    print(nomes)
    
for posicao, nomes in enumerate(lista):
    print(posicao + 0, nomes)
    
for posicao, nomes in enumerate(lista):
    print(f'{posicao + 1})', nomes)

dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
                  'Quinta', 'Sexta', 'Sábado')

for dia in dias_da_semana:
    print(f'Hoje é {dia}')