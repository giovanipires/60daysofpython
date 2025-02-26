def conversor_de_temperatura():
    print("Bem-vindo ao seu conversor de temperatura!")
    print("Operações disponíveis:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    while True:
        # Solicita ao usuário que escolha uma operação
        operacao = input("Escolha a operação (1 ou 2) ou digite 'sair' para encerrar: ")

        # Verifica se o usuário deseja sair
        if operacao.lower() == 'sair':
            print("Obrigado por usar o conversor. Até mais!")
            break

        # Verifica se a operação é válida
        if operacao not in ['1', '2']:
            print("Opção inválida. Tente novamente.")
            continue

        # Solicita os números ao usuário
        try:
            valor = float(input("Digite o valor a converter: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
            continue

        # Realiza a operação escolhida
        if operacao == '1':
            resultado = (valor * 9/5) + 32
            print(f'O valor de {valor}°C convertido para Fahrenheit_é de ', resultado)
        elif operacao == '2':
            resultado = (valor - 32) * 5/9
            print(f'O valor de {valor}°F convertido para Celsius é de ', resultado)

# Executa o conversor
conversor_de_temperatura()
