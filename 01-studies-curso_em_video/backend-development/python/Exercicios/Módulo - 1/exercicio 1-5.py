opcao = None
while (opcao != 0):
    print("Qual Exercício você deseja fazer?")
    print("0 - Sair")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    print("4 - Exercício 4")
    print("5 - Exercício 5")
    opcao = int(input("Escolha a opção desejada\n"))

    if (opcao == 1):
        print("==== Exercício 1 ====")
        msg_e1 = "Olá, Mundo!"
        print(msg_e1)

    elif (opcao == 2):
        print("==== Exercício 2 ====")
        nome_e2 = input("Qual é o seu nome?\n")
        print("Prazer em te conhecer, {}".format(nome_e2))
    # Isso faz com que na hora que escramos dentro da {} {}".format(nome_e2)
 
    elif (opcao == 3):
        print("==== Exercício 3 ====")
        print("Somando dois números")
        n1 = int(input("Digite um número "))
        n2 = int(input("Digite outro número "))
        print(n1+n2)

    elif (opcao == 4):
        print("==== Exercício 4 ====")
        print("Comparando tipo primitivo de Dados")
        texto = input("Digite algo: ")
        print("Esse texto é ",type(texto))
        print("Esse texto só tem espaços?", texto.isspace())
        print("Esse texto é um número?",texto.isnumeric())
        print("Esse texto é alfabético?",texto.isalpha())
        print("Esse texto é alfanumérico?",texto.isalnum())
        print("Esse texto está em maiúsculo?",texto.isupper())
        print("Esse texto está em minúsculo",texto.islower())
        print("Esse texto está Capitalizado? (Tanto Maiúsculo quanto menúsculo)",texto.istitle())
       
    elif (opcao == 5):
        print("==== Exercício 5 ====")
        print("Somando dois números e mostrando seu antecessor e sucessor")
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        soma = n1 + n2
        print("A soma de {} e {} é {}".format(n1,n2,soma))
        print("O antecesor de {} é {}".format(soma,soma-1))
        print("O sucessor de {} é {}".format(soma,soma+1))
       

    elif (opcao == 0):
        print("Saindo do Programa...")

    else:
        print("Opção Inválida - Tente novamente")
    
