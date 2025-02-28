"""Exercício sobre contador de vogais"""

print("Bem vindo(a) ao contador de vogais com Python.")

def contar_vogais(palavra):
    # Definindo as vogais
    vogais = "aeiouAEIOU"
    
    # Inicializando o contador
    contador = 0
    
    # Percorrendo cada caractere da palavra
    for letra in palavra:
        # Verificando se a letra é uma vogal
        if letra in vogais:
            contador += 1
    
    # Retornando o total de vogais
    return contador

# Solicita ao usuário que digite uma palavra
palavra = input("Digite uma palavra: ")

# Chama a função e exibe o resultado
quantidade_vogais = contar_vogais(palavra)
print(f"A palavra '{palavra}' tem {quantidade_vogais} vogais.")
