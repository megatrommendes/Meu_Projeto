def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

def main():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (1922-2021): "))
            ano_atual = 2022  # Supomos que o ano atual seja 2022
            if 1922 <= ano_nascimento <= 2021:
                idade = calcular_idade(ano_nascimento, ano_atual)
                print(f"Nome: {nome_completo}")
                print(f"Idade: {idade} anos")
                break
            else:
                print("Ano de nascimento fora do intervalo válido (1922-2021).")
        except ValueError:
            print("Ano de nascimento inválido. Digite um número válido.")

if __name__ == "__main__":
    main()
