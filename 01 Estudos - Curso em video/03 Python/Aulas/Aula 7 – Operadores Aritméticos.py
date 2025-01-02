def Tipos_de_formatacao():
    nome = input("Qual é o seu nome? ")
    print("Prazer em te conhecer {:>10}!".format(nome))  # Alinhamento à direita
    print("Prazer em te conhecer {:^20}!".format(nome))  # Alinhamento ao centro
    print("Prazer em te conhecer {:=^20}!".format(nome), end=" ")  # Alinhamento ao centro com '='
    print("você tem um bom nome")  # 'end' junta com a próxima linha de print


def Calculadora():
    while True:
        opcao_calc = MenuCalc()

        if opcao_calc == 1:
            print("Você escolheu Somar")
            n1 = int(input("Digite um número: "))
            n2 = int(input("Digite outro número: "))
            soma = n1 + n2
            print("A soma é {}".format(soma))
        elif opcao_calc == 2:
            print("Você escolheu Subtrair")
            n1 = int(input("Digite um número: "))
            n2 = int(input("Digite outro número: "))
            subtrair = n1 - n2  
            print("A subtração é {}".format(subtrair))
        elif opcao_calc == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente!")

        continuar = input("Você deseja continuar? (S/N): ").upper()  # Converte a resposta para maiúsculas
        if continuar == "N":
            print("Saindo...")
            break
            


def MenuCalc():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")
    return int(input("Escolha uma das opções acima: "))  # Retorna a opção escolhida como inteiro


def Menu():
    print("1 - Acessar o exercício Tipos de formatação")
    print("2 - Acessar a Calculadora")
    print("3 - Sair do Programa")
    return int(input("Escolha uma das opções acima: "))  # Retorna a opção escolhida como inteiro

# Quando você usa return em uma função, ele "devolve" um valor, que pode ser usado por outra variável fora da função. Essa variável pode armazenar o valor retornado e utilizá-lo em outras partes do código.
while True:
    opcao = Menu()

    if opcao == 1:
        Tipos_de_formatacao()
    elif opcao == 2:
        Calculadora()
    elif opcao == 3:
        print("Saindo do Programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")
