#trabalhando com listas Aula 6

#lista simples
# frutas = ["acerola", "abacaxi", "abacate", "amora"]
# print(frutas)

# #imprimindo uma a uma com um for
# for fruta in frutas:
#     print(fruta)
    
#criando uma nova lista com inclusão
frutas = []
while True:
    fruta = input("Digite uma fruta: ")
    if fruta == "sair" or fruta == "Sair":
        break
    frutas.append(fruta)
    
print(frutas)