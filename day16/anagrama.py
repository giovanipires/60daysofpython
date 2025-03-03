"""Criando um anagrama"""
def anagrama(palavra1, palavra2):
    """_summary_
    Verifica se duas palavras são anagramas ou não
    Args:
        palavra1 (string): Uma palavra
        palavra2 (string): Uma palavra
        return: True se as palavras forem um anagrama
    """
    #Removendo espaços e convertendp para letras minúsculas
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavras, {palavra1} e {palavra2} são anagramas."
    return f"Essas palavras, {palavra1} e {palavra2} não são anagramas."

print("Bem vinda ao verificador de anagramas")
contexto_01 = input("Digite a primeira palavra: ")
contexto_02 = input("Digite a segunda palavra: ")

palavra1 = contexto_01
palavra2 = contexto_02

print(anagrama(palavra1, palavra2))
