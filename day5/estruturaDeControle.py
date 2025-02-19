#condicional
# com base em uma condição
# if elif else

# idade = 17
# if idade >= 18:
#     print('Maior de idade.')
# else:
#     print('Menor de idade!')
    
# poder = 9000
# if poder > 8000:
#     print('É mais de 8000!')
# elif poder > 7000: #se e senão
#     print('É mais de 7000!')
# elif poder > 6000:
#     print('É mais de 6000!')
# else:
#     print('Ainda está baixo.')

# Loops
# for while

#condicional dentro de um loop
# personagens = ["Naruto", "Sasuke", "Sakura"]
# for ninjas in personagens:
#     if ninjas == "Sakura":
#         print(ninjas + " é uma ninja de Konoha")
#     else:
#         print(ninjas + " é um ninja de Konoha")
        
# contador = 0
# while contador < 3:
#     print('Treinamento')
#     print(contador)
#     contador += 1 
    
#controles de fluxo
# break continue pass

# for i in range(10):
#     if i == 5:
#         break
#     print(i)
    
# for x in range(10):
#     if x == 2:
#         continue
#     print(x)
 
# personagens = ["Naruto", "Sasuke", "Sakura"]
# for ninjas in personagens:
#     if ninjas == "Sakura":
#         continue
#     else:
#         print(ninjas + " é um ninja de Konoha")
        
# for x in range(10):
#     if x == 5:
#         pass #serve como um placeholder
#     print(x)

# nivelPoder = 50
# while nivelPoder < 8000:
#     print('Treinando...')
#     nivelPoder += 500
#     print(nivelPoder)
#     print('Não é possível Kakaroto, ele está poderoso!')
    
senha = "Tr3inam3nt0"
tentativa = 3
while tentativa > 0:
    entrada_senha = input("Digite a senha para acessar: ")
    if entrada_senha == senha:
        print('Acesso liberado!')
        break #pausar o loop
    else:
        tentativa -=1
        print(f"Senha incorreta, tentativas restantes: {tentativa}")
else:
    print("Tentativa esgotadas, acesso bloqueado.")