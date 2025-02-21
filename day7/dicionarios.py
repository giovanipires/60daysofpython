dicionario = {
    "Fabricante": "Nissan",
    "Concessionária": "Daisa",
    "Chassi": "391839391839",
    "Veículo": "Kicks",
    "Modelo": "Evolution"
}

carro = dicionario

print(carro)
print(dicionario["Chassi"])
print(dicionario)

dicionario["Ano"] = 2023

print(dicionario)
print(dicionario["Ano"])

if "Ano" in dicionario:
    print("Esta chave está no dicionário")
else:
    print("Chave não localizada.")
    
if "Acessórios" in dicionario:
    print("Esta chave está no dicionário")
else:
    print("Chave não localizada.")
    
del dicionario["Concessionária"]

print(dicionario)

carro_key = dicionario.keys()
print(carro_key)

carro_value = dicionario.values()
print(carro_value)
print(dicionario.items())
print(dicionario.get("Veículo"))
print(dicionario.get("Num.donos", "Não existe!"))
print(dicionario.get("Num.donos"))

for chave in dicionario.keys():
    print(chave)
    
for value in dicionario.values():
    print(value)
    
for key, value in dicionario.items():
    print(key, value)