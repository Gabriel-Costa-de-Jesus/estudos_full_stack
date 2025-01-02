#Inicio do programa - Cadastro de usários

#Solicitação ao usuário da quantidade a serem cadastradas
quantidadeUsuarios = int(input("Quantos usuários deseja cadastrar?")) #LER Um dado digitado ao usuário

#Declaração de variáveis 
nomes = [""] * quantidadeUsuarios #vetor dinamico nome[quantidadeUsuarios]
idades =[0] * quantidadeUsuarios  
emails =[""] * quantidadeUsuarios  
usuarios_cadastrado = 0
i=0

#Função o menu
def exibir_menu():
    print("\n Menu")
    print("1- Cadastrar novo usuário")
    print("2 - Listar todos os usuários")   
    print("3 - Buscar usuário pelo nome")   
    print("4 - Sair do sistema") 
    return  int(input("Escolher uma opção: ")) #LER

def buscar_usuario(nome_procurado):
    for i in range(quantidadeUsuarios): #percorre todos os usuários cadastrados dentro do vetor
        if nomes[i] == nome_procurado:
            print(f"Usuário encontrado: Nome= {nomes[i]}, Idade= {idades[i]}, E-mail= {emails[i]}")
            break
        else:
            print("Usuário não cadastrado")
    return


#Inicio do loop principal 
while True: #ESTRUTURA DE REPECIÇÃO
    opcao = exibir_menu() #Chamando minha função e recebendo na variáveil opcao o dado digitado pelo usuário
    
    #ESTRUTURA DE CONDIÇÃO
    if (opcao==1): #Lógica SE para cadastrar um novo usuário
        if usuarios_cadastrado<quantidadeUsuarios: #verificando se ainda há espaço para mais cadastrados
            nome = input(f"Digite o nome do usuário {usuarios_cadastrado + 1}: ") #recebendo o nome digitado
            idade = int(input("Digite o idade do usuário: "))   #recebendo a idade digitada
            email = input("Digite o email do usuário: ")        #recebendo o email
            
            nomes[usuarios_cadastrado] = nome           #guardando os dados no vetor
            idades[usuarios_cadastrado] = idade
            emails[usuarios_cadastrado] = email
            
            #Atualiza o número de usuários cadastrados
            usuarios_cadastrado += 1 #incremento 

            print("Usuário {nome}, {idade}, {email} foram cadastrados com sucesso")
    
    elif (opcao==2): #Listar os usuários cadastrados
        if usuarios_cadastrado == 0:        #estamos verificando se há usuários cadastrados
            print("Não há usuários cadastrados") #mostrando na tela os usuários
        else:
            for i in range(usuarios_cadastrado):
                print(f"\n Nome: {nomes[i]}, Idade: {idades[i]}, E-mail: {emails[i]}")

    elif (opcao==3): #Buscar um valor digitado 
        nome_procurado = input("Digitar o nome do usuário que deseja buscar:")
        buscar_usuario(nome_procurado)
                       
    elif (opcao==4):
        print("Saindo do programa...")
        break #Saindo do loop do programa

    else:
        print("Opção inválida e encerra o programa")







