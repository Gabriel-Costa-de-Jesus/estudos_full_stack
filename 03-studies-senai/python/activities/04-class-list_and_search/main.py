class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
usuarios = []

def exibirMenu():
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario por Nome")
    print("4 - Sair do sistema")

def cadastrarUsuario():
    nome = input("Infome o nome: \n")
    idade = int(input("Informe a idade: \n"))
    usuario = Usuario(nome, idade) #Adicionar informação a classe
    usuarios.append(usuario) #Adicionar informação no vetor
    
    print("Usuário cadastrado com sucesso!")

def listarUsuarios():
    print("***** Usuários cadastrados *****")
    for usuario in usuarios:
        print("Nome: ", usuario.nome, usuario.idade, "\n")
        
def buscarUsuario():
    procurar_usuario = input("Digite o usuário para ser procurado no sistema \n")
    encontrado_usuario = False
    for usuario in usuarios:
        if (procurar_usuario == usuario.nome):
            print("Este usuário está cadastrado no sistema! Usuário", usuario.nome, usuario.idade, "Anos")
            encontrado_usuario = True

    if (encontrado_usuario == False):
        print("Este usuário não está cadastrado")

quantidade_maxima_usuarios = int(input("Informe a quantidade máxima de usuários que deseja: \n"))

while(True):

    exibirMenu()

    opcao_menu = int(input("Informe a opção desejada? \n"))

    if (opcao_menu == 1):
        if (quantidade_maxima_usuarios == len(usuarios)):
            print("Atingiu a quantidade máxima de usuários!!!!")
        else:
            cadastrarUsuario()
    if (opcao_menu == 2):
        listarUsuarios()
    if (opcao_menu == 3):
        buscarUsuario()
    if (opcao_menu == 4):
        break
