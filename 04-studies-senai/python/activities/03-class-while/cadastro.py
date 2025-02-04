print("Olá seja bem-vindo(a) ao programa")

qtd_pessoas = int(input("Digite o número de pessoas que serão cadastradas: "))

opcao = 0
contador = 0
usuarios_cadastrados = []

while (opcao != 3):
    print("\nO que você deseja fazer?")
    print("Opção 1 - Cadastrar novo usuário")
    print("Opção 2 - Listar todos os usuários cadastrados")
    print("Opção 3 - Sair do Programa")
    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):
        if (contador < qtd_pessoas):
            usuario = input("Digite o nome do usuário: ")
            usuarios_cadastrados.append(usuario)
            contador += 1
            print("Usuário cadastrado com sucesso!")
        else:
            print("Limite de usuários atingido.")

    elif (opcao == 2):
        if (usuarios_cadastrados):
            print("Usuários cadastrados:")
            for usuario in usuarios_cadastrados:
                print(usuario)
        else:
            print("Nenhum usuário cadastrado ainda.")

    elif (opcao == 3):
        print("Você escolheu a opção de Sair. Programa encerrado.")

    else:
        print("Opção inválida! Tente novamente.")
