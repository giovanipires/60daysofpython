"""Gerador de senhas"""

import random
import string

def gerador_de_senhas(tamanho):
    """Função para gerar senhas aleatórias e temporárias com base no tamanho definido"""
    comprimento = int(tamanho)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
    print(f"Sua senha temporária gerada foi: {senha}")

gerador_de_senhas(12)