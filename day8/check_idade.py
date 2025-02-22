"""Module providing a function printing python version."""
#Solicitar a idade e verificar se o mesmo pode dirigir

idade = int(input("Por favor digite sua idade: "))

if idade >= 18:
    print("Você pode dirigir.")
    habilitado = input("Você possui habilitação: ")
    if habilitado == "Sim" or habilitado == "sim":
        print("Obrigado por cooperar, boa viagem!")
    else:
        print("Seu veículo será apreendido e você será multado.")
else:
    print("Você não pode dirigir, seu veículo será apreendido e você será multado.")
