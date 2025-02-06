usuarios = []
Contar_Usuarios = 0
indice = 0
def exibirMenu():
    print("\n" + "--"*30)
    print("Escolha uma das opções abaixo: \n")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario por Nome")
    print("4 - Sair do sistema")
    print("5 - Remover um usuário")
    print("--"*30)

def cadastrarUsuario():
    if (Contar_Usuarios < quantidade_maxima_usuarios):
        print("--"*30)
        
        nome = input("Infome o nome do Usuário {}: \n".format(indice))
        idade = int(input("Informe a idade do Usuário {}: \n".format(indice)))
        usuario = Usuario(nome, idade, indice) #Adicionar informação a classe
        usuarios.append(usuario) #Adicionar informação no vetor
        
        print("Usuário cadastrado com sucesso!")
        print("--"*30)
    else:
        print("Você atingiu a capacidade máxima de Usuários no sistema.\nPor Favor, Remova um usuário do Sistema para continuar!")

def listarUsuarios():
    print("--"*30)
    print("***** Usuários cadastrados *****")
    for usuario in usuarios:
        print("Nome do Usuário {}:".format(usuario.indice), usuario.nome, usuario.idade, "anos\n")
    print("--"*30)    

def buscarUsuario():
    print("--"*30)
    procurar_usuario = input("Digite o usuário para ser procurado no sistema: \n")
    for usuario in usuarios:
        if (procurar_usuario == usuario.nome):
            print("Este usuário está cadastrado no sistema! Usuário {}".format(usuario.indice), usuario.nome, usuario.idade, "Anos")
            break
    else:
        print("Este usuário não está cadastrado")

    print("--"*30)
    
def Sair():
    print("Saindo do Sistema...")

def RemoverUsuario():
    print("--"*30)
    Remover_o_Usuario = input("Digite o nome do usuário para ser Removido: \n")
    for usuario in usuarios:
        if (Remover_o_Usuario == usuario.nome):
            print(usuario.nome,"Usuário Removido com Sucesso!")
            usuarios.remove(usuario)
            break
    else:
        print("Digite o nome do Usuário correto!")
    print("--"*30)
    
class Usuario:
    def __init__(self, nome, idade, indice):
        self.nome = nome
        self.idade = idade
        self.indice = indice

print("\n" + "--"*30)
print("Olá seja bem vindo (a) ao nosso sistema de Usuários!")
quantidade_maxima_usuarios = int(input("Informe a quantidade máxima de usuários que deseja: \n"))
print("--"*30)
while(True):

    exibirMenu()
    opcao_menu = int(input("Informe a opção desejada: \n"))

    if (opcao_menu == 1):
        indice += 1
        cadastrarUsuario()
        Contar_Usuarios += 1
    elif (opcao_menu == 2):
        listarUsuarios()
    elif (opcao_menu == 3):
        buscarUsuario()
    elif (opcao_menu == 4):
        Sair()
        break
    elif (opcao_menu == 5):
        RemoverUsuario()
        Contar_Usuarios -= 1
    else:
        print("Opção Inválida! Tente Novamente")