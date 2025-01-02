print("Olá seja bem vindo (a) ao programa")

qtd_pessoas = int(input("Digite o número de pessoas que irá ser cadastrada "))

opcao = 0
contador = 0
usuarios_cadastrados = " "
while (opcao != 3):
    
    print("O que você deseja fazer?")
    print("Opção 1 - Cadastrar novo usuário")
    print("Opção 2 - Listar todos os usuários cadastrados")
    print("Opção 3 - Sair do Programa")
    opcao = int(input())

    if opcao == 1:
        if contador < qtd_pessoas:
            contador = contador+1
            print("Você escolheu a opção de cadastrar o usuário")
            usuario = input("Digite o nome do usuário ")
            usuarios_cadastrados += usuario
        else:
            print("Limite de usuários atinjidos")  
    elif opcao ==2:
        print("Você escolheu a opção de Listar usuários Cadastrados") 
        print("Usuários Cadastrados", usuarios_cadastrados)
    elif opcao ==3:
        print("Você escolheu a opção de Sair") 
    else:
        print("Opção inválida")