#listas mão na massa, aula 9.1

#listas podem ser modificadas
#tuplas não podem ser modificadas
#conjutos não possuem ordem nem podem se duplicar dados

# lista = [1, 2, 3, 4]
# print(lista)

# lista2 = list("1234")
# print(lista2)

# lista3 = ['texto', 469, 11.5, True, False, [1, 2, 3]]
# print(lista3)
# print(lista3[0])
# print(lista3[3])
# print(lista3[-1])
# print(lista3[-1][1])
# lista3.append('Kick')
# print(lista3)
# lista3[2] = 13
# print(lista3)

# lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista4)
# del lista4[0]
# print(lista4)
# print(lista4[0:3])
# lista4.append(11)
# print(lista4)
# lista4 += [12]
# print(lista4)

# lista5 = [1, 2]
# um, dois = lista5
# print(um)
# print(dois)

# for i in lista5:
#     print(i)
    
# for i in lista5:
#     print(i+1)

# lista6 = ["Cachorro", "Gato", "Peixe"]
# lista7 = ["Porco", "Cavalo", "Sapo"]

# lista_6_7 = zip(lista6, lista7)
# print(tuple(lista_6_7))

# for l6, l7 in zip(lista6, lista7):
#     print(l6, l7)
    
# print(len(lista6))

#Métodos

# lista8 = [1, 2, 3, 4]
# print(lista8)
# lista8.append(5)
# print(lista8)
# lista8.extend([6, 7, 8])
# print(lista8)
# lista8.insert(0, 99)
# print(lista8)
# del lista8[0]
# print(lista8)
# lista8.insert(1, 1.5)
# print(lista8)
# lista8.remove(1.5)
# print(lista8)
# lista8.pop()
# oito = lista8.pop()
# print(lista8)
# print(oito)

# lista9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista9.reverse()
# print(lista9)

# lista10 = [99, 76, 14, 22, 6 , 8]
# lista10.sort()
# print(lista10)
# lista10.sort(reverse=True)
# print(lista10)

animais = ["Burro", "Mula", "Jegue", "Cavalo", "Égua", "Ponei"]
print(animais)
print(animais.index("Jegue"))
