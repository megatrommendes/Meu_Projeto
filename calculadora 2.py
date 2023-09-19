def calculadora():
    while True:
        print("Selecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação: ")

        if escolha == "0":
            print("Saindo da calculadora.")
            break
        elif escolha in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                resultado = num1 + num2
            elif escolha == "2":
                resultado = num1 - num2
            elif escolha == "3":
                resultado = num1 * num2
            elif escolha == "4":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Erro: divisão por zero")
                    continue

            print("Resultado:", resultado)
        else:
            print("Essa opção não existe. Tente novamente.")

# Chama a função calculadora para iniciar o programa
calculadora()
