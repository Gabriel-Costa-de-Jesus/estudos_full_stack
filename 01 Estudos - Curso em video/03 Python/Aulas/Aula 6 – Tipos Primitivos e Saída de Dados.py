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
        n1 = int(input("Digite um número\n"))
        n2 = int(input("Digite outro número\n"))
        print("A soma de {} e {} é {}".format(n1,n2,n1+n2))

    elif (opcao == 2):
        print("==== Desafio 2 ====")
        print("Tipos de dados")
        nome_d2 = str("Gabriel")
        idade_d2 = int(19)
        altura_d2 = float(1.75)
        peso_d2 = str("75 kg")
        sexo_d2 = bool('M')

        print(type(nome_d2), nome_d2)
        print(type(idade_d2), idade_d2)
        print(type(altura_d2), altura_d2)
        print(type(peso_d2), peso_d2)
        print(type(sexo_d2), sexo_d2)

    elif (opcao == 3):
        print("==== Desafio 3 ====")
        print("Tipos de dados 2")
        nome_d3 = input("Digite seu nome")
        idade_d3 = int(input("Digite sua idade"))
        altura_d3 = float(input("Digite sua altura"))
        peso_d3 = str(input("Digite seu peso"))
        sexo_d3 = bool(input("Digite seu sexo"))

        print(type(nome_d3), nome_d3)
        print(type(idade_d3), idade_d3)
        print(type(altura_d3), altura_d3)
        print(type(peso_d3), peso_d3)
        print(type(sexo_d3), sexo_d3)

    elif (opcao == 0):
        print("Saindo do Programa...")
        break
    else:
        print("Opção Inválida - Tente novamente")
    
