#Funções em Python
#funções nativas do python
# len()
# min()
# max()
# print()

#criando uma função
# def nome_funcao():
#     return 

# def subtracao(numeros):
#     numero = 0
#     for n in numeros:
#         numero -= n
#     return numero

# print(subtracao([100, 50, 25]))

# def soma1(*numeros): #transformei em uma tupla, isso vai afetar diretamente como chamar a função
#     numero = 0
#     for n in numeros:
#         numero += n
#     return numero

# print(soma1(15, 16, 100))


# def divisao(a, b):
#     return a / b

# print(divisao(9, 3))

# def multiplicacao(a, b):
#     return a * b

# print(multiplicacao(5, 10))

# def hello_nome(nome):
#     print(f"Hello {nome}")
    
# hello_nome('Luiz')

# def soma2(**numeros): #transformamos em um opção de chave valor
#     print(type(numeros))
#     numero = 0
#     for key, value in numeros.items():
#         print(key, value)
#         numero += value
#     return print(numero)
    
# soma2(
#     primeiro=1,
#     segundo=2,
#     terceiro=3,
#     quarto=4,
#     quinto=5
# )

def somaComMedia(a: int,b: int) -> int: #doc string
    """
        Função que recebe dois números e retorna a soma e a média entre eles.
    """
    soma = a + b
    media = soma / 2
    return print(soma, media)

somaComMedia(6, 2)

# help(somaComMedia)
print(somaComMedia.__annotations__)
