opcao = None
while (opcao != 0):
    print("Qual desafio você deseja fazer?")
    print("0 - Sair")
    print("1 - Desafio 1")
    print("2 - Desafio 2")
    print("3 - Desafio 3")
    opcao = int(input("Escolha a opção desejada\n"))

    if (opcao == 1):
        print("==== Desafio 1 ====")
        nome_d1 = input("Olá, qual é o seu nome? \n")
        print("Olá", nome_d1, "Prazer em te conhecer!")

    elif (opcao == 2):
        print("==== Desafio 2 ====")
        dia_d2 = input("Em que dia você nasceu?\n")
        mes_d2 = input("Em que mês você nasceu?\n")
        ano_d2 = input("Em que ano você nasceu?\n")
        print("Você nasceu no dia", dia_d2, "no mês de", mes_d2, "no ano de", ano_d2)

    elif (opcao == 3):
        print("==== Desafio 3 ====")
        n1 = int(input("Digite um número\n"))
        n2 = int(input("Digite outro número\n"))
        print("A soma deles é:", n1+n2)

    elif (opcao == 0):
        print("Saindo do Programa...")

    else:
        print("Opção Inválida - Tente novamente")
    
