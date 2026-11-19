from math import factorial


def main():
    while True:
        print("------------------------------")
        print("Mini Calculadora")
        print("1-Somar dois números")
        print("2-Subtrair dois números")
        print("3-Multiplicar dois números")
        print("4-Dividir dois números")
        print("5-Fatorial de um número")
        print("6-Potência entre dois números")
        print("7-Sair\n")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "7":
            break
        if opcao not in {"1", "2", "3", "4", "5", "6"}:
            print("Opção inválida. Escolha um número de 1 a 7.")
            continue

        try:
            if opcao == "5":
                numero = int(input("Digite um inteiro não negativo: "))
                print(f"O fatorial de {numero} é {factorial(numero)}")
                continue

            primeiro = float(input("Digite o 1° número: "))
            segundo = float(input("Digite o 2° número: "))

            if opcao == "1":
                print(f"A soma de {primeiro} e {segundo} é {primeiro + segundo}")
            elif opcao == "2":
                print(f"A subtração de {primeiro} e {segundo} é {primeiro - segundo}")
            elif opcao == "3":
                print(f"A multiplicação de {primeiro} e {segundo} é {primeiro * segundo}")
            elif opcao == "4":
                print(f"A divisão de {primeiro} e {segundo} é {primeiro / segundo}")
            elif opcao == "6":
                print(f"{primeiro} elevado a {segundo} é {primeiro ** segundo}")
        except ValueError:
            if opcao == "5":
                print("Use um inteiro não negativo dentro do limite de exibição do Python.")
            else:
                print("Número inválido. Use ponto para valores decimais.")
        except ZeroDivisionError:
            print("Não é possível fazer uma divisão por zero.")
        except OverflowError:
            print("O resultado é grande demais para esta operação.")

    print("------------------------------")
    print("Fim da Calculadora")


if __name__ == "__main__":
    main()
