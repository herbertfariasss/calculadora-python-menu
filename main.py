#Calculadora simples com while
controle = 1

print("------------------------------", end="\n")
while True:
    print("Mini Calculadora")
    print("1-Somar dois números")
    print("2-Subtrair dois números")
    print("3-Multiplicar dois números")
    print("4-Dividir dois números")
    print("5-Fatorial de um número")
    print("6-Potência entre dois números")
    print("7-Sair\n")
    controle = int(input("Escolha uma opção: "))
    if (controle == 7):
        break
    print("------------------------------", end="\n")
    
    #opções
    if controle == 1:
        num1 = float(input("Digite o 1° número: "))
        num2 = float(input("Digite o 2° número: "))
        print(f"\aA soma de {num1} e {num2} é {num1 + num2}")
        print("------------------------------", end="\n")
    
    elif controle == 2:
        num1 = float(input("Digite o 1° número: "))
        num2 = float(input("Digite o 2° número: "))
        print(f"\aA subtração de {num1} e {num2} é {num1 - num2}")
        print("------------------------------", end="\n")
    
    elif controle == 3:
        num1 = float(input("Digite o 1° número: "))
        num2 = float(input("Digite o 2° número: "))
        print(f"\aA multiplicação de {num1} e {num2} é {num1 * num2}")
        print("------------------------------", end="\n")
    
    elif controle == 4:
        num1 = float(input("Digite o 1° número: "))
        num2 = float(input("Digite o 2° número: "))
        if num2 == 0:
            print("Não é possível fazer a divisão por zero")
            print("------------------------------", end="\n")
        else:
            print(f"\aA divisão de {num1} e {num2} é {num1 / num2}")
            print("------------------------------", end="\n")
    
    elif controle == 5:
        num1 = float(input("Digite um número: "))
        fatorial = 1
        contador = num1
        while contador>1:
            fatorial *= contador
            contador-=1
        print(f"\aO fatorial de {num1} é {fatorial}")
        print("------------------------------", end="\n")
                
    elif controle == 6:
        num1 = float(input("Digite o número base: "))
        num2 = float(input("Digite o número a elevar: "))
        print(f"\n {num1} elevado a {num2} é {num1 ** num2}")
        print("------------------------------", end="\n")

print("------------------------------", end="\n")        
print("Fim da Calculadora")