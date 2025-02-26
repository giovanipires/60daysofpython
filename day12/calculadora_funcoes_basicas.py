def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    while True:
        # Solicita ao usuário que escolha uma operação
        operacao = input("Escolha a operação (1/2/3/4) ou digite 'sair' para encerrar: ")

        # Verifica se o usuário deseja sair
        if operacao.lower() == 'sair':
            print("Obrigado por usar a calculadora. Até mais!")
            break

        # Verifica se a operação é válida
        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue

        # Solicita os números ao usuário
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
            continue

        # Realiza a operação escolhida
        if operacao == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif operacao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")

# Executa a calculadora
calculadora()
