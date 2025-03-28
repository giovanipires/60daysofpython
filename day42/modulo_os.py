import os

diretorio = "./"
arquivos_pasta = os.listdir(diretorio)
# print(arquivos_pasta)

for pastas in arquivos_pasta:
    caminho_completo = os.path.join(diretorio, pastas)
    if os.path.isdir(caminho_completo):
        print(f"Pasta que esta sendo verificada {pastas}")
        print(os.listdir(pastas))

for arquivos in arquivos_pasta:
    caminho_completo = os.path.join(diretorio, arquivos)
    if os.path.isfile(caminho_completo):
        print(f"Verificando o diretório se contem arquivos em {arquivos_pasta}")
        print(arquivos)
