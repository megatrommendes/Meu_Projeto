def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se o divisor não é zero
            resultado = num1 / num2
        else:
            resultado = 0
    else:
        resultado = 0  # Número de operação inválido
    
    return resultado

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(numero1, numero2, operacao)

if resultado == 0:
    print("Operação inválida ou divisão por zero.")
else:
    print("Resultado:", resultado)
