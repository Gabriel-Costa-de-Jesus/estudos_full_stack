opcao = None  # Variável global inicialmente definida como None
usuarios = [] 
def saudacoes():
    print("Seja bem vindo (a)! O objetivo desta atividade é criar um banco de dados")

def menu():
    print("--" * 30)
    print("O que você deseja fazer?")
    print("1 - Cadastrar usuário")
    print("2 - Exibir usuário cadastrado")
    print("3 - Remover um usuário")
    print("4 - Buscar um usuário")
    print("5 - Alterar senha cadastrada")
    print("6 - Sair do Sistema")
    opcao = int(input("Escolha uma opção acima: "))  # Converte para int
    print("--" * 30)
    return opcao  # Retorna o valor de opcao

def cadastro():
    print("--" * 30)
    nome = str(input("Digite o nome do usuário para ser cadastrado: "))
    senha = str(input("Digite a senha do usuário para ser cadastrada: "))
    idade = int(input("Digite a idade do usuário para ser cadastrada: "))
    cep = int(input("Digite o nome da cidade do usuário para ser cadastrada: "))
    info_usuario = usuarioclass(nome,senha,idade,cep)
    usuarios.append(info_usuario)
    print("Usuário Cadastrado com sucesso!")
    print("--" * 30)

def lista():
    print("--" * 30)
    print("Usuários cadastrados no sistema:")
    for info_usuario in usuarios:
        print(info_usuario.nome)
    print("--" * 30)

def remover():
    print("--" * 30)
    usuario_remove = input("Digite o nome do usuário para ser removido do Sistema: ")
    encontrado = False  # Flag para verificar se o usuário foi encontrado
    for usuario in usuarios:
        if usuario.nome == usuario_remove:
            usuarios.remove(usuario)  # Remove o usuário da lista
            print(f"Usuário {usuario.nome} removido com sucesso!")
            encontrado = True
            break  # Sai do loop após encontrar e remover o usuário
    if not encontrado:
        print(f"Usuário {usuario_remove} não encontrado.")
    print("--" * 30)

def sair():
     print("--" * 30)
     print("Saindo do Sistema...")
     print("--" * 30)

class usuarioclass:
    def __init__(self, nome,senha,idade,cep):
        self.nome = nome
        self.senha = senha
        self.idade = idade
        self.cep = cep
saudacoes()

while True:
    opcao = menu()  # Captura o valor retornado da função menu
    if (opcao == 1):
        cadastro()
    elif (opcao == 2):
        lista()
    elif (opcao == 3):
        remover()
    elif (opcao == 6):
        sair()
        break
    else:
        print("Opção inválida, tente novamente.")
