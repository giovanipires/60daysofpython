produto = {'nome': 'Caneta Bic', 'preco': 3.99,
           'importada': False, 'estoque': 999}
for chave in produto:
    print(chave)
    
for valor in produto.values():
    print(valor)
    
for chave, valor in produto.items():
    print(f'{chave} : {valor}')